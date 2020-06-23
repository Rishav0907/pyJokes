import requests
import random
import pyfiglet
header=pyfiglet.figlet_format('JOKES')
print(header)
url="https://icanhazdadjoke.com/search"
term=input("What jokes would you like to search for?")
res=requests.get(url,
                 headers={"Accept":"application/json"},
                params={"term":term}).json()
num=res['total_jokes']
if num>1:
    j=random.randint(0,num)
    jokes=res["results"]
    print(f"I found {num} jokes about {term}. Here's one:")
    for i in jokes:
        print(jokes[j]['joke'])
        break
elif num<=1:
    print("I found  joke")
    print(res["results"][0])
else:
    print("No jokes")