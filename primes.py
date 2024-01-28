"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    lst = []
    current_number = 2
    while len(lst) < number_of_primes:
        is_prime = True
        for prime in lst:
            if current_number % prime == 0:
                is_prime = False
        if is_prime:
            lst.append(current_number)

        current_number += 1

    return lst


print(primes(12))
