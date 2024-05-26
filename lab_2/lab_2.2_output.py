class User:
    def __init__(self, name, age, user_type, full_phone):
        self.name = name
        self.age = age
        self.user_type = "Engineer" if user_type == 1 else "Manager"
        self.full_phone = full_phone

    def print_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Type:", self.user_type)
        print("Phone:", self.full_phone)

# Виклик класу
user = User("John", 25, 1, "+0509379992")
user.print_details()
