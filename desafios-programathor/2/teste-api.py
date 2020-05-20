import requests

newstories_response = requests.get('https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty').json()

i = 0
while i < len(newstories_response) && prox == True:
    
    id_item1 = newstories_response[0]
    id_item2 = newstories_response[1]
    id_item3 = newstories_response[2]
    id_item4 = newstories_response[3]
    id_item5 = newstories_response[4]

