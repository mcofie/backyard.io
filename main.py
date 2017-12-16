'''
Author: Maxwell Cofie
Project: backyard.io
Date Started: 10th Agust 2017
'''
#imports
import uuid
import pymysql
import urllib as url

hostname = 'localhost'
username = 'root'
password = 'boss1234'
database = 'backyard_io'


con = pymysql.connect( hostname, username, password, database )

def init( conn ):
    cur = conn.cursor()
    
    cur.execute( "SELECT * FROM account_details limit 1" )
    if(len(cur.fetchall()) == 0):
      set_up(conn)
    else:
      print "You're most welcome!"
      status(conn)


def set_up(conn):
  cur = conn.cursor()
  print ("Welcome to backyard.io")
  
  first_name = raw_input("Please enter Firstname: ")
  last_name  = raw_input("Please enter Lastname: ")
  country  = raw_input("Country: ")
  pass_word = raw_input("Password: ")
  location  = raw_input("City: ")

  username  =  generate_token(7)
  query = "insert into account_details (first_name,last_name,username, pass_word, location, country) values (%s,%s,%s,%s,%s,%s)"
  cur.execute(query,(first_name,last_name,username,pass_word,location,country))
  conn.commit()
  



def authentication(user_name,pass_word):
  if(username == user_name and password == pass_word):
      return True
  else:
      return False


def status(conn):
    cur = conn.cursor()
    cur.execute( "SELECT username FROM account_details limit 1" )
    access_token = cur
    for i in cur:
        print 'Access Token :', i[0] +"'\n" + 'Soil moisture : ', get_soil_moisture()+"\n"+'Soil Temperature : ',get_soil_temperature()+"\n"+ 'Light Intensity : ',get_light_intensity()+"\n"+network_status()
        


def get_soil_moisture():
   return "940 vol" #temporary placeholders


def get_soil_temperature():
  return "13 Celcius" #temporary placeholders


def get_light_intensity():
  return "89 lx" #temporary placeholders


def generate_token(size=13):
  random = str(uuid.uuid4())
  random = random.upper()
  random = random.replace("-","")
  return random[0:size]



def network_status():
    try:
        url.request.urlopen("https//:google.com")
        return "Active Connection"
    except:
        return "Connection Failed"



#Call Main Function

init( con )
con.close()





















