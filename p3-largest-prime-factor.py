def print_problem():
    print("The prime factors of 13195 are 5, 7, 13 and 29. " +
          "What is the largest prime factor of the number 600851475143?")


def initialize(number):
    list_numbers = list()

    for i in range(2, number + 1):
        if number % i == 0:
            list_numbers.append(i)

    return list_numbers


def exclude_not_prime(list_numbers, limit):
    for number in list_numbers:
        factor = number
        while factor <= limit:
            factor = factor + number
            try:
                list_numbers.remove(factor)
            except ValueError:
                pass

    return list_numbers


def get_largest_prime_factor(number):
    list_numbers = initialize(number)
    list_numbers = exclude_not_prime(list_numbers, number)
    return list_numbers.pop()


print_problem()
print(get_largest_prime_factor(600851475143))
