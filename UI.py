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
    session.session.close()
    raise SystemExit

    user_input = input()
    while user_input != "end":
        if user_input not in range(1,5):
            print("Incorrent input")
            continue
        session.get_courses(user_input)

        user_input = input()

if __name__ == "__main__":
    main()