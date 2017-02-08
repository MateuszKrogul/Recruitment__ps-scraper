import Session
def main():
    print("Username: ")
    username = input()
    print("Password: ")
    password = input()

    print("Type \"end\" to close.")

    session = Session.Session()
    session.login(username,password)

    terms = session.get_terms()
    for term in terms :
        print("{} - {}".format(term, terms[term][0]))
    print("Choose term: ")

    user_input = input()
    while user_input != "end":
        if user_input == "end": break
        try:
            term = int(user_input)
        except:
            print("Incorrent input")
            user_input = input()
            continue
        if term not in range(1,6):
            print("Incorrent input")
            user_input = input()
            continue
        courses = session.get_courses(term)


        for i in range(len(courses[term])):
            print("{} - {}".format(i, courses[term][i][0]))
        print("Choose course:")

        user_input = input()
        while user_input != -1:
            if user_input == "end": break
            try:
                course = int(user_input)
            except:
                print("Incorrent input")
                user_input = input()
                continue
            if course not in range(0,len(courses[term])+1):
                print("Incorrent input")
                user_input = input()
                continue

            grade = session.get_grade(term,course)
            print("{} -> grade: {}".format(courses[term][course][0], grade))
            user_input = -1

        user_input = input()

if __name__ == "__main__":
    main()
    #TODO serve bad login or password