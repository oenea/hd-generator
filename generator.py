from faker.providers import internet
import csv
import uuid
import random
from faker import Faker
from datetime import datetime, timedelta, date
import faker_commerce

fake = Faker("pl_PL")
fake.add_provider(faker_commerce.Provider)

num_products = 100  # Number of products
num_months = 12     # Number of months to simulate data for

def main():
    products = [{'id': str(uuid.uuid4()), 'name': fake.ecommerce_name().capitalize()} for _ in range(num_products)]

    sheet1_data = []
    sheet2_data = []

    for month in range(1, num_months + 1):
        for product in products:
            product_name = product['name']
            units_sold = random.randint(1, 100)
            price_per_unit = round(random.uniform(5, 100), 2)
            date = datetime(datetime.now().year, month, 1).strftime('%y/%m')
            
            sheet1_data.append({
                'Product name': product_name,
                'Number of units sold': units_sold,
                'Price of a single unit': price_per_unit,
                'Date': date
            })
            
            for _ in range(units_sold):
                sale_date = datetime(datetime.now().year, month, random.randint(1, 28)).strftime('%Y-%m-%d')
                sheet2_data.append({
                    'Product id': product['id'],
                    'Date of sale': sale_date,
                    'Product name': product_name
                })

    with open('Sheet1_Product_Sales_Info.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Product name', 'Number of units sold', 'Price of a single unit', 'Date'])
        writer.writeheader()
        writer.writerows(sheet1_data)

    with open('Sheet2_Individual_Product_Sales.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Product id', 'Date of sale', 'Product name'])
        writer.writeheader()
        writer.writerows(sheet2_data)

    print("Sales data generation complete.")

if __name__ == "__main__":
    main()
