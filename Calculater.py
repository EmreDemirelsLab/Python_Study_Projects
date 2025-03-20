def add(x: int | float, y: int | float) -> int | float:
    return x + y

def subtract(x: int | float, y: int | float) -> int | float:
    return x - y

def multiply(x: int | float, y: int | float) -> int | float:
    return x * y

def divide(x: int | float, y: int | float) -> int | float:
    if y == 0:
        return 'Error: Division by zero'
    return x / y

def get_user_input() -> tuple:
    try:
        x = int(input('Enter first number: '))
        y = int(input('Enter second number: '))
        return x, y
    except ValueError:
        print('Invalid input, please enter a number..!')
        return None, None

def calculator():
    while True:
        print('Select an operation: ')
        print('1: Addition')
        print('2: Subtraction')
        print('3: Multiplication')
        print('4: Division')
        print('5: Exit')

        choice = input('Enter your choice (1/2/3/4/5): ')

        if choice == '5':
            print('Exiting...')
            break

        if choice in ['1', '2', '3', '4']:
            x, y = get_user_input()
            if x is None or y is None:
                continue
            if choice == '1':
                print(f'Result: {add(x, y)}')
            elif choice == '2':
                print(f'Result: {subtract(x, y)}')
            elif choice == '3':
                print(f'Result: {multiply(x, y)}')
            elif choice == '4':
                print(f'Result: {divide(x, y)}')
        else:
            print('Invalid operation..! Please enter a valid choice..!')

calculator()
