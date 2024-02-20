"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie

author: Markéta Svěráková Wallo
email: marketa.wallo@gmail.com
discord: marketasverakova_37252
"""
# import ...

separator = "-" * 50

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
    if (user["name"] == login_name.lower() and
        user["password"] == login_password.lower()):
        user_found = True
        break

if user_found:
    print(f"""{separator}
          \n Welcome to the app, {login_name.capitalize()}!
          \n We have 3 texts to be analyzed.
          \n {separator} """
          )
   
else:
    print(f"""{separator}
          \n Terminating the program."""
          )    

# texts    
TEXTS = ["""
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. """,
"""At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.""",
"""The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present."""
]

selected_text = input("Enter a number from 1 to 3:")
if selected_text.isnumeric() and int(selected_text) <= len(TEXTS):
    analyzed_text = TEXTS[int(selected_text)]
else: 
    print(f"""{separator}
          \n Terminating the program."""
          )    
    
# stats  
cleaned_text = list()
for word in analyzed_text.split():
    cleaned_text.append(word.strip(".,:;"))

word_count = len(cleaned_text)

titlecase_words = list()
uppercase_words = list()
lowercase_words = list()
numbers = list()

for word in cleaned_text:
    if word.istitle():
        titlecase_words.append(word)
    elif word.isupper():
        uppercase_words.append(word)
    elif word.islower():
        lowercase_words.append(word)  
    elif word.isnumeric():
        numbers.append(word)

titlecase_word_count = len(titlecase_words)
uppercase_word_count = len(uppercase_words)
lowercase_word_count = len(lowercase_words)
numbers_count = len(numbers)
numbers_sum = sum(int(number) for number in numbers)
print(numbers_sum)

# for number in numbers:
#     int(number)
