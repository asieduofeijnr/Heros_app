import re as r
import json


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