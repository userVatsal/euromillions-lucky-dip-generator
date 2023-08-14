import random
import pandas as pd
from collections import Counter
from typing import List, Tuple
import logging

# Configuration dictionary for constraints
CONFIG = {
    "main_numbers_count": 5,
    "lucky_stars_count": 2,
    "main_numbers_range": (1, 50),
    "lucky_stars_range": (1, 12),
    "even_count_range": (2, 3),
    "odd_count_range": (2, 3),
    "low_count_range": (2, 3),
    "high_count_range": (2, 3),
}

def is_valid_combination(numbers: List[int], number_range: Tuple[int, int]) -> bool:
    """Check if the combination of numbers is valid."""
    if not all(number_range[0] <= num <= number_range[1] for num in numbers):
        return False
    if any(numbers[i] + 1 == numbers[i + 1] for i in range(len(numbers) - 1)):
        return False
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = len(numbers) - even_count
    if not CONFIG["even_count_range"][0] <= even_count <= CONFIG["even_count_range"][1]:
        return False
    if not CONFIG["odd_count_range"][0] <= odd_count <= CONFIG["odd_count_range"][1]:
        return False
    low_count = sum(1 for num in numbers if num <= number_range[1] // 2)
    if not CONFIG["low_count_range"][0] <= low_count <= CONFIG["low_count_range"][1]:
        return False
    return True

def generate_ticket(freq: Counter, k: int = 5) -> List[int]:
    """Generate a ticket based on the frequency of numbers."""
    numbers, weights = zip(*freq.items())
    weights = [weight / sum(weights) for weight in weights]
    numbers = sorted(random.choices(numbers, k=k, weights=weights))
    while not is_valid_combination(numbers, CONFIG["main_numbers_range"] if k == CONFIG["main_numbers_count"] else CONFIG["lucky_stars_range"]):
        numbers = sorted(random.choices(numbers, k=k, weights=weights))
    return numbers

def generate_numbers(data: pd.DataFrame, columns: List[str], k: int = 5) -> List[int]:
    """Generate numbers based on historical data and given columns."""
    frequency = data[columns].stack().value_counts()
    return generate_ticket(frequency, k)

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """Clean data by clipping values within valid ranges."""
    for i in range(1, CONFIG["main_numbers_count"] + 1):
        data[f'Ball {i}'] = data[f'Ball {i}'].clip(lower=CONFIG["main_numbers_range"][0], upper=CONFIG["main_numbers_range"][1])
    for i in range(1, CONFIG["lucky_stars_count"] + 1):
        data[f'Lucky Star {i}'] = data[f'Lucky Star {i}'].clip(lower=CONFIG["lucky_stars_range"][0], upper=CONFIG["lucky_stars_range"][1])
    return data

def main():
    logging.basicConfig(level=logging.INFO)
    try:
        logging.info("Starting the EuroMillions Lucky Dip Generator...")
        url = "https://raw.githubusercontent.com/userVatsal/euromillions-lucky-dip-generator/main/euromillions-draw-history.csv"
        data = pd.read_csv(url)
        data = clean_data(data)

        main_numbers_columns = [f'Ball {i}' for i in range(1, CONFIG["main_numbers_count"] + 1)]
        lucky_star_columns = [f'Lucky Star {i}' for i in range(1, CONFIG["lucky_stars_count"] + 1)]

        main_numbers = generate_numbers(data, main_numbers_columns)
        lucky_stars = generate_numbers(data, lucky_star_columns, k=CONFIG["lucky_stars_count"])

        print("Main Numbers:", main_numbers)
        print("Lucky Stars:", lucky_stars)

        logging.info("Exiting the EuroMillions Lucky Dip Generator.")
    except pd.errors.EmptyDataError:
        logging.error("The data file is empty.")
    except pd.errors.ParserError:
        logging.error("There was an error parsing the data file.")
    except Exception as e:
        logging.error("An unexpected error occurred: %s", str(e))

if __name__ == "__main__":
    main()


