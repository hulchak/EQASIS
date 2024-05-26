class ShapeCalculator:
    def calculate_area(self, shape):
        print("Area:", shape.calculate_area())

# Використання
circle = Circle(5)
calculator = ShapeCalculator()
calculator.calculate_area(circle)
