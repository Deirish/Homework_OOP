from employees.empl_exceptions import EmailAlreadyExistsException


class Employee:
    def __init__(self, name, salary, email):
        self.name = name
        self.salary = salary
        self.email = email
        self.validate()
        self.save_email()

    def save_email(self):
        with open('emails.txt', 'a+') as fp:
            fp.write(self.email.lower() + '\n')

    def validate(self):
        with open('emails.txt', 'r') as fp:
            if self.email.lower() in fp.read():
                raise EmailAlreadyExistsException('Email exists in file!')




