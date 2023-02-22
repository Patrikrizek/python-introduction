# Getting input
# This task focuses on getting input from the user to make the code more dynamic.
# Write a simple computer program that asks a user to input their name and email address, and then displays a message that tells the person that you will be contacting them using the email address they entered.
# For example:
# If a user enters Mike as their name and mike@example.com as their email, the output would be:
# Hi Mike! We will be contacting you shortly at mike@example.com

name = input("Please enter your name:")
email_address = input("Please enter your email:")

print("Hi " + name + "! We will be contacting you shortly at " + email_address)
