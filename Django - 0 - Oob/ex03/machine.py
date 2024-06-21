import random

from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.count = 10
    class EmptyCup(HotBeverage):
        name = "empty cup"
        price = 0.90
        def description(self):
            return bcolors.OKCYAN + "An empty cup?! Gimme my money back!"
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__(bcolors.FAIL + "This coffee machine has to be repaired." + bcolors.ENDC)
    def repair(self):
        self.count = 10
        return "Machine is broken, attempting to repair..."
    def serve(self, name):
        if issubclass(name, HotBeverage):
            if (self.count > 0):
                if random.choice([True, False]):
                    self.count -= 1
                    return name()
                else:
                    self.count -= 1
                    return self.EmptyCup()
            else:
                raise self.BrokenMachineException()
            
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main():
    try:
        
        machine = CoffeeMachine()
        list = [Coffee, Chocolate, Tea, HotBeverage, Cappuccino]
        for i in range(25):
            try:
                print(bcolors.OKGREEN)
                print(i + 1)
                print(machine.serve(random.choice(list)))
            except machine.BrokenMachineException as e:
                print(bcolors.WARNING + machine.repair())
                print(bcolors.OKCYAN + "Machine repaired")
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()