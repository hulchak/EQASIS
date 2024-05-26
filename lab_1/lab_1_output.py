def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_median(numbers):
    numbers_sorted = sorted(numbers)
    mid_index = len(numbers) // 2
    if len(numbers) % 2 == 0:
        return (numbers_sorted[mid_index - 1] + numbers_sorted[mid_index]) / 2
    return numbers_sorted[mid_index]

def calculate_min(numbers):
    return min(numbers)

def calculate_max(numbers):
    return max(numbers)

def compute_statistics(numbers):
    if not numbers:
        return None

    mean = calculate_mean(numbers)
    median = calculate_median(numbers)
    minimum = calculate_min(numbers)
    maximum = calculate_max(numbers)

    return {
        "mean": mean,
        "median": median,
        "minimum": minimum,
        "maximum": maximum
    }
