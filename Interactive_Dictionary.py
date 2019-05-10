## Program Name: My Dictionary
## Created by: Syed Mudassir Ali
## Description:
## This is a dictionary application, where user will give an input.
## Application will intelligently give list of all possible words, 
## and also take confirmation from user whether they want to see suggestion list or not.
## If user gives 'Y', suggestion list will appear otherwise application will move forward
## and return meanings of the given word.
## Application will also cater if there is any typo error from user while entering the word.
## User do not need to worry for word's case sensitivity. Application will accept word in any case.


import json  ## Used to read/write JSON file
from difflib import get_close_matches ## To list words in case of any mistake in spelling
import re ## I used 're' here to list all possible matches

data = json.load(open("data.json"))

word = input("Give Word: ")
word = word.lower()


def my_dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),n=5,cutoff=0.8)) > 0:
        yn = input("You mean %s. Press Y for yes, or N for no: " % get_close_matches(w,data.keys(),n=5,cutoff=0.8)[0])
        if yn == 'Y':
            return data[get_close_matches(w,data.keys(),n=5,cutoff=0.8)[0]]
        else:
            return "Please enter word again."
            
    else:
        return "Please give correct word."

## Here taking an input word to match suggestions

regex = re.compile(get_close_matches(word,data.keys())[0])
matches = [string for string in data if re.match(regex, string)]

## Giving option to user if they need any suggestion

ask_suggestion = input("Would you like suggestions matching your given word. Press 'Y' for yes, or 'N' for no: ")

## The block which will work based upon the response given by user in above part.

## If user input 'Y' for suggestion it will give words suggestion list, and ask user to give input from suggestion list.
if ask_suggestion == 'Y':
    if type(matches) == list:
        for item in matches:
            print(item)
    else:
        print(matches)
    if len(matches) > 0:
        sw = input("Type your word from above list: " % matches)
        output = my_dictionary(sw)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)
    else:
        output = my_dictionary(sw)
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)

## If user input 'N' for suggestion it will not give words suggestion list.
else:
    output = my_dictionary(sw)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
    
