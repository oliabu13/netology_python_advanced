import salary
import people
from datetime import datetime
import netflix


def main():
    print("Ну что ж, начнем!")
    salary.calculate_salary()
    people.get_employees()


if __name__ == '__main__':
    main()
    print(f'Дата: {datetime.today()}')
