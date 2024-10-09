import random


def main():
    total = 0
    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """

    while total <= 100:
        number = random.randint(1, 10)
        total += number
        numbers.append(number)
        


    print(f'The random values are {numbers}')
    print(f'The total is {total}')
    print ("sum of numbers less than 100: ", sum(numbers) - numbers[-1])

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
