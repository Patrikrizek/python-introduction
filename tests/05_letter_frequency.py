# For this challenge, create a program that determines the number of occurrences of each letter in the quote "You can have data without information, but you cannot have information without data.", and output a list with each letter and its frequency.
# For this task, you will also need to remember what you’ve learned about lists, as well as some additional understanding of a concept not previously discussed in this trial: for loops.
# Remember that a list is an ordered sequence of elements that can be modified or changed. Each element inside of a list is called an item. Lists enable you to keep similar data together, condense your code, and perform the same methods and operations on multiple values at once. In Python, lists are created by placing items, separated by commas, between square brackets []. Lists work similarly to strings; you use square brackets [] to access data and the first element has an index of 0. The values or items in a list can be strings, integers, floats, other lists or a mix of different types.

# Pseudocode:
    # Create a variable to store the given string "You can have data without information, but you cannot have information without data."
    # Convert the given string to lowercase
    # Create a list containing every lowercase letter of the English alphabet 

    # for every letter in the alphabet list:
    #     Create a variable to store the frequency of each letter in the string and assign it an initial value of zero
    #     for every letter in the given string:
    #         if the letter in the string is the same as the letter in the alphabet list
    #             increase the value of the frequency variable by one.
    #     if the value of the frequency variable does not equal zero:
    #         print the letter in the alphabet list followed by a colon and the value of the frequency variable

aString = "You can have data without information, but you cannot have information without data."
aString.lower()

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

occurrence = [
    (alphabet[i], aString.count(alphabet[i]))
    for i in range(len(alphabet))
    if aString.count(alphabet[i])
]

for letter, frequency in occurrence:
    print(letter,":", frequency)
