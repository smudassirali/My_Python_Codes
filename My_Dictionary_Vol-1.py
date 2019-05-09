import json
from difflib import get_close_matches

data = json.load(open("data.json"))

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

word = input("Give Word: ")

output = my_dictionary(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

    
