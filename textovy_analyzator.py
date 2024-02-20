"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie

author: Markéta Svěráková Wallo
email: marketa.wallo@gmail.com
discord: marketasverakova_37252
"""
# import ...

# login
registered_users = [
    {"name": "bob", "password": "123"},
    {"name": "ann", "password": "pass123"},
    {"name": "mike", "password": "password123"},
    {"name": "liz", "password": "pass123"},
]

login_name = input("Name:")
login_password = input("Password:")

user_found = False

for user in registered_users:
    if user["name"] == login_name and user["password"] == login_password:
        print(f"Welcome to the app, {login_name.capitalize()}!")
        user_found = True
        break

if user_found:
    print(f"Welcome to the app, {login_name.capitalize()}!")
else:
    print("Terminating the program.")    