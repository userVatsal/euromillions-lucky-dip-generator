import random
import pandas as pd
from collections import Counter

# Function to check if the combination is valid
def is_valid_combination(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    if even_count < 2 or even_count > 3:
        return False
    low_count = sum(1 for num in numbers if num <= 25)
    if low_count < 2 or low_count > 3:
        return False
    for i in range(4):
        if numbers[i] + 1 == numbers[i + 1]:
            return False
    return True

# Function to check if the combination is a popular sequence
def is_popular_sequence(numbers):
    return all(numbers[i] + 1 == numbers[i + 1] for i in range(4))

# Function to generate ticket without avoiding previous winning combinations
def generate_ticket_without_avoiding_winners(main_freq, lucky_star_freq):
    main_numbers_pool = [num for num, freq in main_freq.items() for _ in range(freq)]
    lucky_star_pool = [num for num, freq in lucky_star_freq.items() for _ in range(freq)]
    main_numbers = []
    while not main_numbers or not is_valid_combination(main_numbers) or is_popular_sequence(main_numbers):
        main_numbers = sorted(random.sample(main_numbers_pool, 5))
    lucky_stars = sorted(random.sample(lucky_star_pool, 2))
    return main_numbers, lucky_stars

# Load the historical EuroMillions draw data
file_path = "C:\Users\userV\Downloads\euromillions-draw-history.csv" # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Analyze the frequency of main numbers and lucky stars
main_numbers_frequency = Counter(data[f'Ball {i+1}'].values.flatten() for i in range(5))
lucky_star_frequency = Counter(data['Lucky Star 1'].append(data['Lucky Star 2']))

# Generate the lucky dip ticket without avoiding previous winning combinations
no_avoid_main_numbers, no_avoid_lucky_stars = generate_ticket_without_avoiding_winners(main_numbers_frequency, lucky_star_frequency)

print("Main Numbers:", no_avoid_main_numbers)
print("Lucky Stars:", no_avoid_lucky_stars)
