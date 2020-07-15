"""
O(n) - Linear Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


def print_animals(animal_list):  # O(n * 1) = O(n)
    for i in range(len(animal_list)):  # O(n)
        print(animal_list[i])  # O(1)


"""
What about this one? What runtime complexity is this one?
"""


def print_animals(animal_list):  # O(n * (1 + 1 + (100000 * 1))) = O(100002n) = O(n)
    for i in range(len(animal_list)):  # O(n)
        print(animal_list[i])  # O(1)
        my_number = 0  # O(1)
        for _ in range(100000):  # O(100000)
            my_number += 1  # O(1)


"""
CFU: Slack Thread: Why doesn't the nested for loop make the time complexity O(n^2)?
"""


"""
O(n^2) & O(n^3) - Polynomial Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


# Print a list of all possible animal pairs
def print_animal_pairs():  # O(n * (n * (1))) = O(n^2)
    for animal_1 in animals:  # O(n)
        for animal_2 in animals:  # O(n)
            print(f"{animal_1} - {animal_2}")  # O(1)


# Print a list of all possible animal triples
def print_animal_triples():  # O(n * n * n * 1) = O(n^3)
    for animal_1 in animals:  # O(n)
        for animal_2 in animals:  # O(n)
            for animal_3 in animals:  # O(n)
                print(f"{animal_1} - {animal_2} - {animal_3}")  # O(1)


# Print a list of all possible animal triples
def print_animal_triples():  # O((n * 1) + (n * n * n * 1)) = O(n + n^3) = O(n^3)
    for animal in animals:  # O(n)
        print(animal)  # O(1)

    for animal_1 in animals:  # O(n)
        for animal_2 in animals:  # O(n)
            for animal_3 in animals:  # O(n)
                print(f"{animal_1} - {animal_2} - {animal_3}")  # O(1)


"""
CFU: Slack Thread
What's the time complexity to print all animal quintuples? What about "ten"tuples?
"""


"""
O(log n) - Logarithmic Time
"""
animals = ['Duck', 'Jackal', 'Hippo', 'Aardvark', 'Cat',
           'Flamingo', 'Iguana', 'Giraffe', 'Elephant', 'Bear']


# free all the animals, half at a time
# (remove them from the array)
def free_animals(animal_list):
    while len(animal_list) > 0:
        animal_list = animal_list[0: len(animal_list) // 2]

# We are reducing by half at each step
# This is the inverse of doubling at each step O(2^n) - Exponential Time


"""
CFU: Slack Thread
What's the worst the number of steps can get for a O(log n) time complexity
algorithm with an input size of 10 million?
"""

