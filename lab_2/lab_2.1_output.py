class UserProfile:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.is_adult = True if age >= 18 else False

class Scores:
    def __init__(self, scores):
        self.scores = scores
        self.total_score = sum(scores)

def calculate_score(user_profile, scores):
    print("Name:", user_profile.name)
    print("Age:", user_profile.age)
    print("Gender:", user_profile.gender)
    print("Height:", user_profile.height)
    print("Weight:", user_profile.weight)
    print("Total Score:", scores.total_score)
    print("Adult:", user_profile.is_adult)

# Виклик функції
user = UserProfile("John", 25, "Male", 175, 70)
scores = Scores([85, 90, 75, 88, 92])
calculate_score(user, scores)
