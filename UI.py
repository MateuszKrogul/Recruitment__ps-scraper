import Session, data
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
        try:
            user_input = int(user_input)
        except:
            print("Incorrent input")
            user_input = input()
            continue
        if user_input not in range(1,6):
            print("Incorrent input")
            user_input = input()
            continue
        courses = session.get_courses(user_input)


        for i in range(len(courses[user_input])):
            print("{} - {}".format(i, courses[user_input][i][0]))
        print("Choose course:")
        session.session.close()
        raise SystemExit
        user_input = input()

if __name__ == "__main__":
    main()