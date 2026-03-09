import csv
import random
from datetime import date

random.seed(42)

DEPARTMENTS = {1: 'Engineering', 2: 'Marketing', 3: 'Sales', 4: 'Finance'}

FISCAL_PERIODS = {}
period_id = 1
for year in [2023, 2024, 2025]:
    for month in range(1, 13):
        FISCAL_PERIODS[(year, month)] = period_id
        period_id += 1

def get_period_id(year, month):
    return FISCAL_PERIODS[(year, month)]

def last_day(year, month):
    if month == 12: return 31
    elif month in [4, 6, 9, 11]: return 30
    elif month == 2: return 29 if year % 4 == 0 else 28
    else: return 31

def random_date(year, month):
    return str(date(year, month, random.randint(1, last_day(year, month))))

def r2(x):
    return round(x, 2)

journal_entries = []
journal_entry_lines = []
entry_id = 1
line_id = 1

def add_entry(entry_date, description, reference, period_id, lines):
    global entry_id, line_id
    journal_entries.append({
        'entry_id': entry_id,
        'entry_date': entry_date,
        'description': description,
        'reference': reference,
        'period_id': period_id,
    })
    for (account_id, department_id, debit, credit, desc) in lines:
        journal_entry_lines.append({
            'line_id': line_id,
            'entry_id': entry_id,
            'account_id': account_id,
            'department_id': department_id,
            'debit_amount': r2(debit),
            'credit_amount': r2(credit),
            'description': desc,
        })
        line_id += 1
    entry_id += 1

revenue_growth = {2023: 1.0, 2024: 1.2, 2025: 1.44}
seasonal = {1: 0.9, 2: 1.0, 3: 1.05, 4: 1.15}

def quarter(month):
    return (month - 1) // 3 + 1

for year in [2023, 2024, 2025]:
    for month in range(1, 13):
        period = get_period_id(year, month)
        q = quarter(month)
        growth = revenue_growth[year]
        sea = seasonal[q]

        base_salaries = {1: 52000, 2: 32000, 3: 38000, 4: 28000}
        for dept_id, base in base_salaries.items():
            amount = r2(base * (1 + (year - 2023) * 0.05))
            add_entry(
                random_date(year, month),
                f'{DEPARTMENTS[dept_id]} Salary {month:02d}/{year}',
                f'SAL-{year}{month:02d}-D{dept_id}',
                period,
                [(9, dept_id, amount, 0, 'Salaries expense'),
                 (1, dept_id, 0, amount, 'Cash paid for salaries')]
            )

        add_entry(
            str(date(year, month, 1)),
            f'Office Rent {month:02d}/{year}',
            f'RENT-{year}{month:02d}',
            period,
            [(10, 4, 8500, 0, 'Monthly office rent'),
             (1, 4, 0, 8500, 'Cash paid for rent')]
        )

        for i in range(random.randint(4, 6)):
            amount = r2(random.uniform(15000, 45000) * growth * sea)
            debit_acc = 1 if random.random() > 0.4 else 2
            add_entry(
                random_date(year, month),
                f'Sales Revenue {month:02d}/{year} #{i+1}',
                f'REV-{year}{month:02d}-{i+1:02d}',
                period,
                [(debit_acc, 3, amount, 0, 'Revenue received'),
                 (7, 3, 0, amount, 'Sales revenue recognised')]
            )

        for i in range(random.randint(3, 4)):
            amount = r2(random.uniform(8000, 25000) * growth * sea)
            add_entry(
                random_date(year, month),
                f'Service Revenue {month:02d}/{year} #{i+1}',
                f'SVC-{year}{month:02d}-{i+1:02d}',
                period,
                [(2, 3, amount, 0, 'AR for service'),
                 (8, 3, 0, amount, 'Service revenue recognised')]
            )

        for i in range(random.randint(3, 4)):
            amount = r2(random.uniform(10000, 30000) * growth)
            add_entry(
                random_date(year, month),
                f'AR Collection {month:02d}/{year} #{i+1}',
                f'ARC-{year}{month:02d}-{i+1:02d}',
                period,
                [(1, 4, amount, 0, 'Cash collected from customers'),
                 (2, 4, 0, amount, 'Accounts receivable cleared')]
            )

        amount = r2(random.uniform(8000, 20000) * growth * sea)
        credit_acc = 1 if random.random() > 0.3 else 4
        add_entry(
            random_date(year, month),
            f'Marketing Campaign {month:02d}/{year}',
            f'MKT-{year}{month:02d}',
            period,
            [(12, 2, amount, 0, 'Marketing campaign spend'),
             (credit_acc, 2, 0, amount, 'Payment for marketing')]
        )

        if month in [1, 4, 7, 10]:
            amount = r2(random.uniform(12000, 22000) * growth)
            add_entry(
                random_date(year, month),
                f'Software Licenses Q{q} {year}',
                f'SW-{year}Q{q}',
                period,
                [(11, 1, amount, 0, 'Quarterly software licenses'),
                 (1, 1, 0, amount, 'Cash paid for software')]
            )

        add_entry(
            str(date(year, month, min(28, last_day(year, month)))),
            f'Loan Repayment {month:02d}/{year}',
            f'LOAN-{year}{month:02d}',
            period,
            [(5, 4, 5000, 0, 'Loan principal repayment'),
             (1, 4, 0, 5000, 'Cash paid for loan')]
        )

equipment = [
    (2023, 3,  'Laptop purchase - Engineering',  15000, 1),
    (2023, 9,  'Server equipment purchase',       35000, 5),
    (2024, 2,  'Office furniture purchase',       12000, 1),
    (2024, 7,  'Development workstations',        28000, 5),
    (2025, 1,  'Video conferencing equipment',    18000, 1),
    (2025, 6,  'Network infrastructure upgrade',  42000, 5),
]
for (year, month, desc, amount, credit_acc) in equipment:
    add_entry(
        random_date(year, month),
        desc,
        f'EQ-{year}{month:02d}',
        get_period_id(year, month),
        [(3, 1, amount, 0, 'Office equipment purchased'),
         (credit_acc, 1, 0, amount, 'Payment for equipment')]
    )

print(f'Journal entries    : {len(journal_entries)}')
print(f'Journal entry lines: {len(journal_entry_lines)}')

with open('seeds/journal_entries.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['entry_id','entry_date','description','reference','period_id'])
    writer.writeheader()
    writer.writerows(journal_entries)

with open('seeds/journal_entry_lines.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['line_id','entry_id','account_id','department_id','debit_amount','credit_amount','description'])
    writer.writeheader()
    writer.writerows(journal_entry_lines)

print('Done. Files written to seeds/')
