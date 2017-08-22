'''
Author: Maxwell Cofie
Project: backyard.io
Date Started: 10th Agust 2017
'''
#imports
import uuid


username = "mcofie";password = "foodwars"

def set_up():
  print ("Welcome to backyard.io")
  _user = input("Please enter username: ")
  _pass = input("Please enter password: ")
  if(authentication(_user,_pass)):
    print ("Access Granted")
  else:
    print ("Access Denied")



def authentication(user_name,pass_word):
  if(username == user_name and password == pass_word):
      return True
  else:
      return False


def get_soil_moisture():
   pass



def get_soil_temperature():
  pass



def get_light_intensity():
  pass


def generate_token(size=10):
  random = str(uuid.uuid4())
  random = random.upper()
  random = random.replace("-","")
  return random[0:size]
  

#Call Main Function
print(generate_token(17))























