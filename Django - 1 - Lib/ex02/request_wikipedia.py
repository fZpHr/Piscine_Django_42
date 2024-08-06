from requests import *
from json import *
from sys import *
import dewiki 

def request_wiki():
    if len(argv) != 2:
        print("Usage: python3 request_wikipedia.py <query>")
        exit(1)
    try:
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "titles": argv[1],
            "prop": "extracts",
            "explaintext": True,
            "format": "json",
        }
        response = get(url, params=params)
        if response.status_code != 200:
            print("Error: HTTP status code", response.status_code)
            exit(1)
        data = response.json()
        for each in data['query']['pages'].values():
            if ('extract' in each and each['extract'] != ''):
                with open(argv[1] + '.wiki', 'w') as file:
                    file.write(dewiki.from_string(each['extract']))
            else:
                print("No result")
                exit(1)
    except Exception as e:
        print("Error:", e)
        exit(1)

if __name__ == '__main__' :
    request_wiki() 