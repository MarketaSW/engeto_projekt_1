"""
textovy_analyzator.py: první projekt do Engeto Online Python Akademie

author: Markéta Svěráková Wallo
email: marketa.wallo@gmail.com
discord: marketasverakova_37252
"""
import sys

separator = "-" * 50

# login
registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123",
    }

login_name = input("Name:")
login_password = input("Password:")

if login_name in registered_users and registered_users[login_name] == login_password:
    print(f"""\n{separator}
          \nWelcome to the app, {login_name.capitalize()}!
          \nWe have 3 texts to be analyzed.
          \n{separator}\n"""
          )   
else: 
    print(f"""{separator}
Unregistered user. Terminating the program."""
          ) 
    sys.exit()    

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

while True:
    selected_text = input("Enter a number from 1 to 3:")
    if selected_text.isnumeric() and 1 <= int(selected_text) <= len(TEXTS):
        analyzed_text = TEXTS[int(selected_text) - 1]
        break
    else:
        print("Try again.")   
        
# stats  
cleaned_text = list()
for word in analyzed_text.split():
    cleaned_text.append(word.strip(".,:;"))

word_count = len(cleaned_text)

titlecase_words = list()
uppercase_words = list()
lowercase_words = list()
numbers = list()
word_lenghts = dict()

for word in cleaned_text:
    if word.istitle() and word[0].isalpha():
        titlecase_words.append(word)
    elif word.isupper():
        uppercase_words.append(word)
    elif word.islower():
        lowercase_words.append(word)
    elif word.isnumeric():
        numbers.append(word) 
    word_lenght = len(word)
    word_lenghts[word_lenght] = word_lenghts.get(word_lenght, 0) + 1       

titlecase_word_count = len(titlecase_words)
uppercase_word_count = len(uppercase_words)
lowercase_word_count = len(lowercase_words)
numbers_count = len(numbers)
numbers_sum = sum(int(number) for number in numbers)

print(f"""
There are {word_count} words in the selected text.
There are {titlecase_word_count} titlecase words.
There are {uppercase_word_count} uppercase words.
There are {lowercase_word_count} lowercase words.
There are {numbers_count} numeric strings.
The sum of all the numbers is: {numbers_sum}.
\n{separator}\n"""
)

# bar chart
occurence_width = max(word_lenghts.values())

print(f"{"LEN": >4} | {"OCCURENCE": ^{occurence_width}} | COUNT")
print(separator)
for lenght,count in sorted(word_lenghts.items()):
    print(f"{lenght: >4} | {("*" * count): <{occurence_width}} | {count}")
