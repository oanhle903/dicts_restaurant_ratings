"""Restaurant rating lister."""


import sys

file_name = sys.argv[1]

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

def process_scores(file_name):
    """Read scores file and return dictionary of {restaurant-name: score}."""

    scores_txt = open(file_name)
    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(':')
        scores[restaurant] = int(score)
    
    return scores


def add_rate(scores):
    """Add a restaurant and rating."""

    print("Please add a rating for your favorite restaurant!")
    restaurant = input("Restaurant name: ")
    rating = get_score("Rating: ")

    scores[restaurant] = rating

def get_score(prompt):
    """Get the valid scores."""

    while True:
        entry = input(prompt)

        # input must be a digit
        if not entry.isdigit():
            continue

        rating = int(entry)
        if rating >= 1 and rating <= 5:
            return rating



def print_scores(scores):
    """Print restaurants and ratings, sorted."""
    
    for restaurant, rating in sorted(scores.items()):
        print(f"{restaurant} is rated at {rating}.")

# read existing scores in from file
scores = process_scores(file_name)

    
while True:

    print("What would you like to do?")
    print("    1: See ratings for all restaurants")
    print("    2: Add a new restaurant")
    print("    3: Quit")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print_scores(scores)
    elif choice == 2:
        add_rate(scores)
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please try again.")
