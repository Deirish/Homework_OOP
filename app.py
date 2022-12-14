from employees.empl_exceptions import EmailAlreadyExistsException
from employees.employee import Employee
import traceback
from datetime import datetime


def main():
    emp1 = Employee('Vasya', 500, 'vasiliy@gmail.com')
    print(emp1)


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        with open('logs.txt', 'a+') as fp:
            message = f'{datetime.now()} {traceback.format_exc()}'
            fp.write(message)
            # fp.write(traceback.format_exc())
