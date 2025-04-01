# Write your code here.

def hello():
    return "Hello!"

def greet(name):
    return f"Hello, {name}!"

def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
    except ValueError: 
        return f"You can't convert {value} into a {data_type}."
    
def grade(*args):
    try:
        average = sum(args) / len(args)
        if average > 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

def repeat(string, count):
    try:
        result = ""
        for i in range(count):
            result += string
        return result
    except TypeError:
        return f"Can't use {string} or/and {count}."
    
def student_scores(positional, **kwargs):
    if positional == "best":
        best_score = 0
        best_student = ""
        for student, score in kwargs.items():
            if score > best_score:
                best_score = score
                best_student = student
        return best_student
    elif positional == "mean":
        return sum(kwargs.values()) / len(kwargs)
    else:
        return "Invalid request"
    
def titleize(text):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = text.split()

    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            result.append(word.capitalize())
        elif word.lower() in little_words:
            result.append(word.lower())
        else:
            result.append(word.capitalize())
    return " ".join(result)
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result = []

    for word in words:
        if word.startswith("qu"):
            result.append(word[2:] + "quay")
        elif word[0] in vowels:
            result.append(word + "ay")
        else:
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    i += 2
                    break
                i += 1
            result.append(word[i:] + word[:i] + "ay")

    return " ".join(result)
