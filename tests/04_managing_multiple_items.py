# You are going to be creating a program that represents the movements of the line for the lady's bathroom. To begin, create a list that represents the line. It must contain the five names of the women initially waiting (you can make these up).
# The following events occur, and you must represent them in the list and print the list out after each action.
    # A woman named Jenny arrives who only wanted to check her lipstick, she asks to join the front of the line, and all the women let her.
    # The woman third in line’s phone started ringing, and she left the line to answer.
    # A new woman named Alice joined the line.

queue =  ["Ema", "Anna", "Jane", "Karen", "Liz"]
print(queue)

queue.insert(0, "Jenny")
print(queue)

queue.pop(0) # Jenny went into the lady's bathroom
queue.pop(2)
print(queue)

queue.pop(0) # Ema went into the lady's bathroom
queue.append("Alice")
print(queue)
