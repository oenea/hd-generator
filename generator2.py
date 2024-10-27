import csv
import uuid
import random
from faker import Faker
from datetime import datetime, timedelta, date
from randomtimestamp import randomtimestamp

fake = Faker()

# number of records
num_employees = 50
num_products = 10000
num_returns = 100000
num_complaints = 10000

def random_date(start_year, end_year):
    return fake.date_between(start_date=date(start_year, 1, 1), end_date=date(end_year, 12, 31))

# generate Employees
employees = []
for _ in range(num_employees):
    employees.append({
        'id': str(uuid.uuid4()),
        'name': fake.name(),
        'birth_year': random_date(1960, 2005).strftime('%Y-%m-%d %H:%M:%S'),
        'employment_start': random_date(2000, 2024).strftime('%Y-%m-%d %H:%M:%S')
    })

# generate Products
products = []
for _ in range(num_products):
    products.append({
        'id': str(uuid.uuid4()),
        'name': fake.word().capitalize(),
        'issue_year': fake.year(),
        'main_building_material': fake.random_element(['Metal', 'Plastic PBT', 'Plastic POM', 'Plastic ABS', 'Wood', 'Glass Fiber', 'Steel', 'Aluminum', 'Glass', 'Fiber'])
    })

# generate Returns
returns = []
for _ in range(num_returns):
    product = random.choice(products)
    employee = random.choice(employees)
    status = fake.random_element(['Pending', 'In Progress', 'Completed', 'Canceled'])
    processing_start = random_date(2000, 2024)
    processing_finished = processing_start + timedelta(days=random.randint(1, 30)) if status == 'Completed' else None
    returns.append({
        'id': str(uuid.uuid4()),
        'product_id': product['id'],
        'status': status,
        'employee_id': employee['id'],
        'company_cost': round(random.uniform(50, 5000), 2),
        'description': fake.sentence(),
        'processing_started': processing_start.strftime('%Y-%m-%d %H:%M:%S'),
        'processing_finished': processing_finished.strftime('%Y-%m-%d %H:%M:%S') if processing_finished else ''
    })

# generate ReturnProcessing
return_processing = []
for _ in range(num_returns):
    ret = random.choice(returns)
    return_processing.append({
        'employee_id': ret['employee_id'],
        'return_id': ret['id']
    })

# generate Complaints
complaints = []
for _ in range(num_complaints):
    ret = random.choice(returns)
    issue_date = random_date(2021, 2023)
    resolve_date = issue_date + timedelta(days=random.randint(1, 10))
    complaints.append({
        'id': str(uuid.uuid4()),
        'return_id': ret['id'],
        'issue_date': issue_date.strftime('%Y-%m-%d %H:%M:%S'),
        'resolve_date': resolve_date.strftime('%Y-%m-%d %H:%M:%S'),
        'complaint': fake.sentence()
    })

def save_to_csv(data, filename, fieldnames):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


save_to_csv(employees, 'employees.csv', ['id', 'name', 'birth_year', 'employment_start'])
save_to_csv(products, 'products.csv', ['id', 'name', 'issue_year', 'main_building_material'])
save_to_csv(returns, 'returns.csv', ['id', 'product_id', 'status', 'employee_id', 'company_cost', 'description', 'processing_started', 'processing_finished'])
save_to_csv(return_processing, 'return_processing.csv', ['employee_id', 'return_id'])
save_to_csv(complaints, 'complaints.csv', ['id', 'return_id', 'issue_date', 'resolve_date', 'complaint'])

print("Data generated.")
