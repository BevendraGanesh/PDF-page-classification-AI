print("script started")
import os
import random

# -----------------------------
# Dataset Configuration
# -----------------------------

BASE_DIR = "dataset"

CLASSES = [
    "invoice",
    "receipt",
    "resume",
    "certificate",
    "report",
    "form"
]

SPLITS = [
    "train",
    "test",
    "validation"
]

# Number of files
FILES_PER_CLASS = {
    "train": 100,
    "test": 20,
    "validation": 20
}

# -----------------------------
# Sample Templates
# -----------------------------

invoice_templates = [
"""
INVOICE

Invoice Number : INV-{id}

Invoice Date : {date}

Customer : {customer}

Company : ABC Technologies

Product : Laptop

Quantity : {qty}

Price : {price}

GST : 18%

Total Amount : {total}

Payment Status : Paid
""",

"""
TAX INVOICE

Invoice ID : {id}

Buyer : {customer}

Seller : XYZ Electronics

Items Purchased :

Keyboard

Mouse

Monitor

Total : {total}

Payment Mode : UPI
"""
]

receipt_templates = [
"""
PAYMENT RECEIPT

Receipt Number : REC-{id}

Customer : {customer}

Amount Paid : {price}

Payment Method : Cash

Status : Successful
""",

"""
SHOP RECEIPT

Store : Reliance Mart

Receipt ID : {id}

Customer : {customer}

Items :

Rice

Oil

Sugar

Total Amount : {total}
"""
]

resume_templates = [
"""
RESUME

Name : {customer}

Education :

B.Tech Computer Science

Skills :

Python

Java

Machine Learning

Projects :

PDF Page Classification AI
""",

"""
CURRICULUM VITAE

Candidate : {customer}

Qualification :

Bachelor of Technology

Skills :

Python

SQL

Data Structures

Experience :

Fresher
"""
]

certificate_templates = [
"""
CERTIFICATE OF COMPLETION

This certificate is awarded to

{customer}

for successfully completing

Artificial Intelligence Course
""",

"""
IBM CERTIFICATE

Awarded To

{customer}

Completed

Python Programming
"""
]

report_templates = [
"""
PROJECT REPORT

Title :

AI PDF Classification

Prepared By :

{customer}

Abstract :

This project classifies PDF pages using AI.
""",

"""
ANNUAL REPORT

Company :

ABC Pvt Ltd

Revenue :

500000

Employees :

120

Status :

Growing
"""
]

form_templates = [
"""
APPLICATION FORM

Name : {customer}

Age : 21

Phone :

9876543210

Address :

Hyderabad
""",

"""
COLLEGE ADMISSION FORM

Student :

{customer}

Branch :

Computer Science

Year :

Third Year
"""
]

templates = {
    "invoice": invoice_templates,
    "receipt": receipt_templates,
    "resume": resume_templates,
    "certificate": certificate_templates,
    "report": report_templates,
    "form": form_templates
}

customers = [
    "Ganesh Naidu",
    "Ravi Kumar",
    "Sai Krishna",
    "Kiran",
    "Mahesh",
    "Teja",
    "Arun",
    "Suresh",
    "Vijay",
    "Rahul"
]
# ------------------------------------------
# Random Data Generator
# ------------------------------------------

def random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    year = random.randint(2022, 2026)
    return f"{day:02d}/{month:02d}/{year}"


def random_price():
    return random.randint(500, 100000)


def random_quantity():
    return random.randint(1, 10)


def random_total(price, qty):
    return price * qty


# ------------------------------------------
# Generate Dataset
# ------------------------------------------

def generate_files():

    print("=" * 50)
    print("Generating AI Dataset...")
    print("=" * 50)

    for split in SPLITS:

        for cls in CLASSES:

            folder = os.path.join(BASE_DIR, split, cls)

            os.makedirs(folder, exist_ok=True)

            count = FILES_PER_CLASS[split]

            for i in range(1, count + 1):

                customer = random.choice(customers)

                price = random_price()

                qty = random_quantity()

                total = random_total(price, qty)

                template = random.choice(templates[cls])

                text = template.format(
                    id=1000 + i,
                    date=random_date(),
                    customer=customer,
                    qty=qty,
                    price=price,
                    total=total
                )

                filename = os.path.join(folder, f"{cls}_{i}.txt")

                with open(filename, "w", encoding="utf-8") as file:
                    file.write(text)

            print(f"✔ {split}/{cls} --> {count} files created")

    print("\nDataset Generated Successfully!")

    print("=" * 50)
    print("Generating AI Dataset...")
    print("=" * 50)

    for split in SPLITS:
        for cls in CLASSES:

            folder = os.path.join(BASE_DIR, split, cls)
            os.makedirs(folder, exist_ok=True)

            count = FILES_PER_CLASS[split]

            for i in range(1, count + 1):

                customer = random.choice(customers)
                price = random_price()
                qty = random_quantity()
                total = random_total(price, qty)

                template = random.choice(templates[cls])

                text = template.format(
                    id=1000 + i,
                    date=random_date(),
                    customer=customer,
                    qty=qty,
                    price=price,
                    total=total
                )

                filename = os.path.join(folder, f"{cls}_{i}.txt")

                with open(filename, "w", encoding="utf-8") as file:
                    file.write(text)

            print(f"✔ {split}/{cls} --> {count} files created")

    print("\nDataset Generated Successfully!")


if __name__ == "__main__":
    generate_files()