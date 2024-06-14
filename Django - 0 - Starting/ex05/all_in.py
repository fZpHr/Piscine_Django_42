import sys

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

def state(argv):
    argv = argv.lower().title()
    for key, value in capital_cities.items():
        if value == argv:
            for key1, value1 in states.items():
                if key == value1:
                    return key1.lower().title()
    return None

def capital_city(argv):
    argv = argv.lower().title()
    if argv in states:
        return capital_cities[states[argv]].lower().title()
    return None
def main():

    if (len(sys.argv) == 2):
        arguments = sys.argv[1].split(',')
        arguments = [arg.strip() for arg in arguments]
        for arg in arguments:
            state_result = state(arg)
            capital_city_result = capital_city(arg)
            if state_result:
                arg = arg.lower().title()
                print(f"{arg} is the capital of {state_result}")
            elif capital_city_result:
                arg = arg.lower().title()
                print(f"{capital_city_result} is the capital of {arg}")
            elif arg:
                print(f"{arg} is neither a capital city nor a state")

if __name__ == "__main__":
    main()