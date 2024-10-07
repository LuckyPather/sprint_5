import random
import string


class PersonGenerator:
    def __init__(self):
        self.name = self.name_generator()
        self.email = self.email_generator()
        self.password = self.password_generator()

    def name_generator(self):
        list_name = ["Константин", "Даниил", "Владислав", "Ольга", "Татьяна"]
        random_name = random.choice(list_name)
        return random_name + str(random.randint(100, 999))

    def email_generator(self):
        list_domains = ["@yandex.ru", "@gmail.com", "@yahoo.com", "@mail.ru"]
        random_domain = random.choice(list_domains)
        return self.name + random_domain

    def password_generator(self):
        upper = random.choice(string.ascii_uppercase)
        lower = "".join(random.choices(string.ascii_lowercase, k=3))
        digits = "".join(random.choices(string.digits, k=3))
        special = random.choice('!@#$%^&*()')
        password = upper + lower + digits + special
        return password


