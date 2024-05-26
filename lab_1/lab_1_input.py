def compute_statistics(numbers):
    if not numbers:
        return None

    # Calculate mean
    total = sum(numbers)
    count = len(numbers)
    mean = total / count

    # Calculate median
    numbers_sorted = sorted(numbers)
    mid_index = count // 2
    if count % 2 == 0:
        median = (numbers_sorted[mid_index - 1] + numbers_sorted[mid_index]) / 2
    else:
        median = numbers_sorted[mid_index]

    # Calculate minimum and maximum
    minimum = numbers_sorted[0]
    maximum = numbers_sorted[-1]

    return {
        "mean": mean,
        "median": median,
        "minimum": minimum,
        "maximum": maximum
    }
