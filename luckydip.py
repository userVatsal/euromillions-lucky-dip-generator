import random
import pandas as pd
from collections import Counter

# Function to check if the combination is valid
def is_valid_combination(numbers):
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    if even_count < 2 or even_count > 3 or odd_count < 2 or odd_count > 3:
        return False
    low_count = sum(1 for num in numbers if num <= 25)
    if low_count < 2 or low_count > 3:
        return False
    return True

# Function to generate ticket considering historical data
def generate_ticket(main_freq, lucky_star_freq):
    main_numbers_pool = [num for num, freq in main_freq.items() for _ in range(freq)]
    lucky_star_pool = [num for num, freq in lucky_star_freq.items() for _ in range(freq)]
    main_numbers = []
    while not main_numbers or not is_valid_combination(main_numbers):
        main_numbers = sorted(random.choices(main_numbers_pool, k=5))
    lucky_stars = sorted(random.choices(lucky_star_pool, k=2))
    return main_numbers, lucky_stars

# Load the historical EuroMillions draw data
url = "https://raw.githubusercontent.com/userVatsal/euromillions-lucky-dip-generator/main/euromillions-draw-history.csv"
data = pd.read_csv(url)

# Analyze the frequency of main numbers and lucky stars
main_numbers_frequency = Counter()
lucky_star_frequency = Counter()
for i in range(1, 6):
    main_numbers_frequency.update(data[f'Ball {i}'].clip(lower=1, upper=50))
for i in range(1, 3):
    lucky_star_frequency.update(data[f'Lucky Star {i}'].clip(lower=1, upper=12))

# Generate the lucky dip ticket considering historical data
main_numbers, lucky_stars = generate_ticket(main_numbers_frequency, lucky_star_frequency)

print("Main Numbers:", main_numbers)
print("Lucky Stars:", lucky_stars)

