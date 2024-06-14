import sys

def main():
    states = {
    "Oregon" : "OR",
    "Alabama" : "AL",
    "New Jersey": "NJ",
    "Colorado" : "CO"
    }

    capital_cities = {
    "OR": "Salem",
    "AL": "Montgomery",
    "NJ": "Trenton",
    "CO": "Denver"
    }
    if len(sys.argv) == 2:
        for key, value in capital_cities.items():
            if value == sys.argv[1]:
                for key1, value1 in states.items():
                    if key == value1:
                        print(key1)
                        break
                break
        else:
            print("Unknown capital city")
if __name__ == "__main__":
    main()