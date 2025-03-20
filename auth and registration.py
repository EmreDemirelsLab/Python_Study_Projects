import string

# User list
users = [
    ('beast', '123'),
    ('savage', '987'),
    ('bear', '567')
]


def is_pwd_valid(password: str) -> bool:
    """Checks if the password is secure."""
    char_set = set(password)

    is_result = (
            len(password) >= 8
            and any(c in string.ascii_uppercase for c in char_set)  # Uppercase letter check
            and any(c in string.ascii_lowercase for c in char_set)  # Lowercase letter check
            and any(c in string.digits for c in char_set)  # Digit check
            and any(c in string.punctuation for c in char_set)  # Special character check
    )

    return is_result


def sign_in(username: str, password: str) -> str:
    """Allows the user to log in."""
    for userName, pwd in users:
        if userName == username and pwd == password:
            return f'Welcome, {username}.'
    return 'Incorrect credentials..!'


def sign_up(username: str, password: str) -> str:
    """Registers a new user."""
    global users  # Declared as global to modify the user list

    for userName, pwd in users:
        if userName == username:  # Username check
            return 'This username is already taken..!'

    if is_pwd_valid(password):  # If the password is valid, add the user
        users.append((username, password))
        return 'Registration completed successfully.'
    return 'Invalid password! Your password must be at least 8 characters long and include at least one uppercase letter, one lowercase letter, one number, and one special character.'


# User attempts to log in
print('Enter your credentials to log in..!')
while True:
    username = input('Username: ')
    password = input('Password: ')

    result = sign_in(username, password)
    print(result)

    if result != 'Incorrect credentials..!':
        break  # Exit loop if login is successful

# New user registration
print('Please enter your new user credentials..!')
while True:
    username = input('Username: ')
    password = input('Password: ')

    result = sign_up(username, password)
    print(result)

    if result == 'Registration completed successfully.':
        break  # Exit loop if registration is successful

# Print the updated user list to check if the new user was added
print("Updated User List:", users)

# New user tries to log in
print('Logging in now..!')
login_result = sign_in(username, password)
print(login_result)
