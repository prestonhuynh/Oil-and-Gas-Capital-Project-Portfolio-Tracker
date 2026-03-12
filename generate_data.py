import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()
np.random.seed(42)
random.seed(42)

NUM_PROJECTS = 50

PROJECT_TYPES = [
    'Well Drilling',
    'Pipeline Construction',
    'Facility Upgrade',
    'Maitenance Turnaround'
]

REGIONS = [
    'Permian Basin',
    'Eagle Ford',
    'Gulf Coast',
    'Midland'
]

STATUSES = ['Completed', 'Active', 'Delayed', 'Over Budeget']

PHASES = ['Planning', 'Drilling/Construction', 'Completion', 'Closeout']

OPERATORS = [fake.company() + ' Energy' for _ in range(10)]
SUBCONTRACTORS = [fake.company() + ' Services' for _ in range(20)]

projects = []

for i in range(NUM_PROJECTS):
    project_type = random.choice(PROJECT_TYPES)
    region = random.choice(REGIONS)
    operator = random.choice(OPERATORS)

    # Costs
    budgeted_cost = round(random.uniform(500_000, 15_000_000), 2)
    cost_overrun_factor = np.random.normal(1.05, 0.15)
    actual_cost = round(budgeted_cost * cost_overrun_factor, 2)

    # Phase cost breakdown (actual cost split across phases)
    phase_splits = np.random.dirichlet(np.ones(4))
    phase_costs = {phase: round(actual_cost * split, 2)
                   for phase, split in zip(PHASES, phase_splits)}
    
    # Dates
    start_date = fake.date_between(start_date='-3y', end_date='-6m')
    planned_duration = random.randint(60, 365)
    planned_end = start_date + timedelta(days=planned_duration)
    delay_days = int(np.random.normal(10, 30))
    actual_end = planned_end + timedelta(days=delay_days)

    # Change orders
    change_order_count = random.randint(0, 8)
    change_order_cost = round(budgeted_cost * random.uniform(0, 0.20)
                              * (change_order_count / 8), 2)
    
    status = random.choice(STATUSES)
    subcontractor = random.choice(SUBCONTRACTORS)

    projects.append({
        'Project_ID': f'OG-{1000 + i}',
        'Project_Name': f'{region} {project_type} {i+1}',
        'Project_Type': project_type,
        'Region': region,
        'Operator': operator,
        'Subcontractor':subcontractor,
        'Status': status,
        'Budgeted_Cost': budgeted_cost,
        'Actual_Cost': actual_cost,
        'Phase_Planning': phase_costs['Planning'],
        'Phase_Drilling_Construction': phase_costs['Drilling/Construction'],
        'Phase_Completion': phase_costs['Completion'],
        'Phase_Closeout': phase_costs['Closeout'],
        'Planned_Start': start_date,
        'Planned_End': planned_end,
        'Actual_End': actual_end,
        'Schedule_Variance_Days': delay_days,
        'Change_Order_Count': change_order_count,
        'Change_Order_Cost': change_order_cost
    })

df = pd.DataFrame(projects)

# Calculated columns
df['Cost_Variance'] = df['Actual_Cost'] - df['Budgeted_Cost']
df['Cost_Variance_Pct'] = round((df['Cost_Variance'] / df['Budgeted_Cost']) * 100, 2)
df['Change_Order_Budget_Impact_Pct'] = round((df['Change_Order_Cost'] / df['Budgeted_Cost']) * 100, 2)
df['On_Time'] = df['Schedule_Variance_Days'].apply(lambda x: 'Yes' if x <= 0 else 'No')

# Export
df.to_csv('oil_and_gas_project_data.csv', index=False)
print(f'Data generated: {len(df)} projects')
print(df.head())