from faker import Faker
from faker.providers import internet
from datetime import timedelta
from datetime import date


fake = Faker(pl_PL)

starting_date_1 = date.fromisoformat('2019-12-01')
ending_date_1 = date.fromisoformat('2023-12-01')

starting_date_2 = date.fromisoformat('2022-12-01')
ending_date_2 = date.fromisoformat('2023-12-01')

def main():
    print(starting_date_1)
    pass

if __name__ == "__main__":
    main()
