import requests, re, data
from bs4 import  BeautifulSoup

class Session:
    def __init__(self):
        self.session = requests.session()
        self.is_logged = False
        self.terms_ids= {}
        self.courses_ids= {}
        # courses_ids structure: courses_ids[term]=[[course_name1, course_id1],[course_name2, course_id2],...]

    def login(self,username,password):
        payload = {
            'licznik': 's',
            'login': username,
            'pass': password
        }
        response = self.session.post("https://ps.ug.edu.pl/login.web", data=payload)
        self.is_logged = True
        return self.session

    def logout(self):
        #TODO implement
        pass

    def get_grade(self,course):
        response = self.session.get("https://ps.ug.edu.pl/getPrzedmioty.web?ajax=true&osobaId=0&semId=10574328&pozaTokiem=&wybierzSemKal=20161")
        response = self.session.get("https://ps.ug.edu.pl/getWyniki.web?ajax=true&przedmiotId="+str(data.courses[course][1])+"&identyfikatorGUI=" + data.courses[course][2])
        response = self.session.get("https://ps.ug.edu.pl/getWyniki.web?chosenTab=3&tabClass=ZakladkiPrzedmiotu"+str(data.courses[course][1])+"&")
        response = self.session.get("https://ps.ug.edu.pl/getWyniki.web?ajax=true&przedmiotId=" + str(data.courses[course][1]) + "&identyfikatorGUI=" + data.courses[course][2])
        soup = BeautifulSoup(response.text,"html.parser")
        try:
            div = soup.select("div[id=tabContentZakladkiPrzedmiotu"+str(data.courses[course][1])+"_3]")
            tr = div[0].table.select("tr")
            try:
                grade = str(float(tr[1].td.text.strip()))
            except:
                grade = tr[1].td.text.strip()

        except:
            grade = "no grade"
        return  grade

    def get_terms(self):
        #TODO save to file to read later
        response = self.session.get("https://ps.ug.edu.pl/wyniki.web")
        soup = BeautifulSoup(response.text, "html.parser")
        degree_course_id = soup.select("a[id*=kier]")[0]["id"]

        sciezkaId = re.search(r"_(.*)", degree_course_id)
        sciezkaId = sciezkaId.group(1)

        wybierzKier = re.search(r"kier(.*)_", degree_course_id)
        wybierzKier = wybierzKier.group(1)

        response = self.session.get("https://ps.ug.edu.pl/osCzasu.web?ajax=true&sciezkaId="+ str(sciezkaId) +"&wybierzKier="+str(wybierzKier)+"&osobaId=0")

        soup = BeautifulSoup(response.text, "html.parser")
        terms = soup.select("div[id*=semNr]")

        counter = 1
        for term in terms:
            id = re.search(r"semNr(.*)", term["id"])
            id = id.group(1)
            self.terms_ids[counter] = [term.text.strip(), str(id)] #key is term name e.g. sem1.
            counter += 1
        return self.terms_ids

    def get_courses(self, term):
        response = self.session.get("https://ps.ug.edu.pl/getPrzedmioty.web?ajax=true&osobaId=0&semId=" + str(self.terms_ids[term][1]))
        with open("r.text","w") as f:
            f.write(response.text)

        soup = BeautifulSoup(response.text, "html.parser")
        container = soup.select("div[id*=divZajec]")

        self.courses_ids[term] = []
        for course in soup.select("div[id*=divZajec]"):
            id = re.search(r"przedmiotId=(.*)&", str(course.div.select("script")[1]))
            id = id.group(1)

            id_gui = re.search(r"divZajec(.*)", course["id"])
            id_gui = id_gui.group(1)

            self.courses_ids[term].extend([[course.div.a.text, str(id), str(id_gui)]])
            #course.div.a.text -> course name
        return self.courses_ids