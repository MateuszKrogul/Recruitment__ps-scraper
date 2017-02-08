import requests, re, data
from bs4 import  BeautifulSoup

class Session:
    def __init__(self):
        self.session = requests.session()
        self.is_logged = False
        self.terms_ids={}

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

        for term in terms:
            id = re.search(r"semNr(.*)", term["id"])
            id = id.group(1)
            self.terms_ids[term.text.strip()] = str(id)
        return self.terms_ids
    def get_courses(self, term):
        pass