import Session, data
def main():
    print("Username: ")
    username = input()
    print("Password: ")
    password = input()

    print("Type \"end\" to close.")

    session = Session.Session()
    session.login(username,password)

    counter = 1
    for term in session.get_terms():
        print("{} - {}".format(counter, term))
    print("Choose term: ")

    user_input = input()
    while user_input != "end":
        if user_input not in range(1,5):
            print("Incorrent input")
            continue
        session.get_courses(user_input)
        
        user_input = input()

if __name__ == "__main__":
    main()