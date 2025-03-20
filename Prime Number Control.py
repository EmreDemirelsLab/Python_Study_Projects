# Prime Number Control

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True

def get_user_input() -> int:
    try:
        number = int(input('Enter a number: '))
        return number
    except ValueError:
        print('Invalid input..! Please enter a valid number.')
        return -1

def print_result(number: int, is_prime_number: bool) -> None:
    if is_prime_number:
        print(f'{number} is a prime number!')
    else:
        print(f'{number} is not a prime number!')

def prime_number_program():
    number = get_user_input()
    if number == 1:
        return  # terminates if the input is invalid

    is_prime_number = is_prime(number)
    print_result(number, is_prime_number)

prime_number_program()
