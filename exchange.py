"""
File: exchange.py
Author: Stephanie Graessle
Date: 2024-12-05
Description: Given every participant in an exchange has a number, randomly
match another correspondant up with their number without repeating numbers.
"""
import random

def unique_shuffle(participants):
    """
    Shuffles a list of numbers with no numbers in the same position as previously.

    Parameters:
    participants (list of int): list of numbers
    
    Returns:
    list of int: shuffled numbers with none in same position
    """
    matches = participants[:] # copy of 'participants' list

    all_unique = False
    while not all_unique:
        for i in range(len(participants)):
            if participants[i] == matches[i]:
                # Make sure person doesn't get their own contribution
                random.shuffle(matches)
                break            
            elif i == len(participants)-1:
                # Reached end of list with no issue
                all_unique = True

    return matches

def main():
    n = input("How many participants are there? ")
    n = int(n)
    participants = list(range(1,n+1))
    matches = unique_shuffle(participants=participants)

    for i in range(len(participants)):
        print(f"{participants[i]}\t{matches[i]}")

if __name__ == "__main__":
    main()