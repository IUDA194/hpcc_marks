from faker import Faker

def generate_password(length : int = 24):
    faker = Faker()
    password = faker.password(length=length, special_chars=False, digits=True, upper_case=True, lower_case=True)
    return password
