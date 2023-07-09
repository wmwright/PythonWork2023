import random

def generate_ec2_names(num_instances):
    allowed_departments = ['Marketing', 'Accounting', 'FinOps']
    
    department = input("Enter your department (Marketing, Accounting, or FinOps): ")
    department = department.capitalize()  # Convert the department name to capitalize the first letter
    
    if department not in allowed_departments:
        print("You should not use this Name Generator.")
        return []
    
    ec2_names = []
    for _ in range(num_instances):
        random_chars = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=6))
        ec2_name = f"{department}-{random_chars}"
        ec2_names.append(ec2_name)
    
    return ec2_names

# Example usage:
num_instances = int(input("Enter the number of EC2 instances: "))
ec2_names = generate_ec2_names(num_instances)
print(ec2_names)
