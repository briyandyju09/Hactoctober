import pyttsx3
import wikipedia
import pyjokes
import random
import requests
import datetime
import os

x=input("Command:")
#Wikipedia
if "wiki" in x: 
  w=input("search what?:")
  try:
    result = wikipedia.summary(w, sentences = 3)
    print(result)
    x=input("Next?:")
  except Exception as e:
    # ... PRINT THE ERROR MESSAGE ... #
    print(e)
    x=input("Next?:")

if "time" in x:
#date and time
  datetime_object = datetime.datetime.now()
  print(datetime_object)
  x=input("Next?:")
if "joke" in x:
#jokes
  My_joke = pyjokes.get_joke(language="en", category="all")
  
  print(My_joke)
  x=input("Next?:")

if "dice" in x: 
#roll a dice
  list1 = [1, 2, 3, 4, 5, 6]
  print(random.choice(list1))
  x=input("Next?:")
if "websearch" in x:
#get data from website
  x=requests.get('https://www.replit.com')

  print(x.text)
  x=input("Next?:")
