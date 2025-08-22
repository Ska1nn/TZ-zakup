from auth import TestLoginAuth

def main():
    bot = TestLoginAuth()
    bot.open_login_page()
    bot.login("tomsmith", "SuperSecretPassword!")
    bot.go_to_registration()
    bot.close(5)

if __name__ == "__main__":
    main()
