# Write your code here.
def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"

def calc(a, b, operation='multiply'):
    try:
        match operation:
            case 'multiply':
                return a * b
            case 'add':
                return a + b
            case 'subtract':
                return a - b
            case 'divide':
                return a / b
            case 'modulo':
                return a % b
            case 'int_divide':
                return a // b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

def data_type_conversion(value, type):
    try:
        if type == "int":
            return int(value)
        elif type == "str":
            return str(value)
        elif type == "float":
            return float(value)
        else:
            return f"Unsupported type: {type}"
    except (TypeError, ValueError): 
        return f"You can't convert {value} into a {type}."

def grade(*args):
    try:
        avg = sum(args) / len(args)
        if avg < 60:
            return "F"
        elif avg < 70:
            return "D"
        elif avg < 80:
            return "C"
        elif avg < 90:
            return "B"
        else:
            return "A"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."
    
def repeat(string, count):
    result = ""
    for i in range(1, count + 1):
        result += string
    return result

def student_scores(position, **kwargs):
    if position == "mean":
        return sum(kwargs.values()) / len(kwargs.values())
    elif position == "best":
        for key, value in kwargs.items():
            if value == max(kwargs.values()):
                return key
            
def titleize(raw_string):
    words = raw_string.split()
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    result = []
    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1:
            word = word.capitalize()
        elif word not in little_words:
            word = word.capitalize()
        result.append(word)
    return " ".join(result)

def hangman (secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

def pig_latin(sentence):
    words = sentence.split()
    vowels = "aeiou"
    result = []
    for word in words:
        if word[0] in vowels:
            new_word = word + "ay"
            
        elif word.startswith("qu"):
            new_word = word[2:] + "quay"
        else:
             for i, letter in enumerate(word):
                if letter in vowels:
                    if letter == "u" and word[i-1] == "q":
                        new_word = word[i+1:] + word[:i+1] + "ay"
                    else:
                        new_word = word[i:] + word[:i] + "ay"
                    break
        result.append(new_word)
    return " ".join(result)