import re as r
import json
import time
import datetime


# Making a regular expression to validate an Email
regexp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

# Function to validate Email
def check(the_email):	
	if(r.fullmatch(regexp, the_email)):
		return True
	else:
		return False
		

#import lottie animations from lottie folder in heros folder
def load_lottiefile(filepath: str):
    with open(filepath, 'r') as file:
        return json.load(file)

#password validator
def validate_password(password):  
    if len(password) < 8:  
        return False  
    if not r.search("[a-z]", password):  
        return False  
    if not r.search("[A-Z]", password):  
        return False  
    if not r.search("[0-9]", password):  
        return False  
    return True  

def validate_password(number):
    if not r.search("[0-9]", number) or 9 <= len(number) <= 11:  
        return False 
    else:
        return True
    
# Create class that acts as a countdown
def countdown(h, m, s):
 
    # Calculate the total number of seconds
    total_seconds = h * 3600 + m * 60 + s
 
    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:
 
        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds = total_seconds)
        
        # Prints the time left on the timer
        print(timer, end="\r")
 
        # Delays the program one second
        time.sleep(1)
 
        # Reduces total time by one second
        total_seconds -= 1
    return True