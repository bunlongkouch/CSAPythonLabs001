# Application 1
def repeat_characters(string):
    repeated_string = ""
    for char in string:
        repeated_string += char * 2
    return repeated_string

string = input("Enter String: ")
print(repeat_characters(string))


#Application 2
def get_letter_range(range_string):
    start, end = range_string.lower().split('-')
    letter_range = ""
    for char_code in range(ord(start), ord(end) + 1):
        letter_range += chr(char_code)
    if range_string.isupper():
        return letter_range.upper()
    return letter_range
user_range = input("Enter a range of letters (e.g., a-z): ")
print(get_letter_range(user_range))