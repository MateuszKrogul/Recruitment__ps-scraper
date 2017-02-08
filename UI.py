import Session, data
def main():
    print("Username: ")
    username = input()
    print("Password: ")
    password = input()

    print("Type \"end\" to close.")

    session = Session.Session()

    user_input = input()
    while user_input != "end":
        try:
            try:
                user_choice = data.courses[user_input][1]
            except:
                print("Incorrect input")
                user_input = input()
                continue
            if not session.is_logged:
                session.login(username,password)
            grade = session.get_grade(user_input)
            print(grade)
            user_input = input()
        except KeyboardInterrupt:
            session.session.close()
    session.session.close()

if __name__ == "__main__":
    main()