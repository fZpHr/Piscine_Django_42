
def main():
    try:
        class HotBeverage:
            price = 0.30
            name = "hot beverage"
            def description(self):
                return "Just some hot water in a cup."
            def __str__(self):
                return f"name : {self.name}\nprice : {self.price:.2f}\ndescription : {self.description()}"
        class Coffee(HotBeverage):
            price = 0.40
            name = "coffee"
            def description(self):
                return "A coffee, to stay awake."
        class Tea(HotBeverage):
            name = "tea"
        class Chocolate(HotBeverage):
            price = 0.50
            name = "chocolate"
            def description(self):
                return "Chocolate, sweet chocolate..."
        class Cappuccino(HotBeverage):
            price = 0.45
            name = "cappuccino"
            def description(self):
                return "Un po’ di Italia nella sua tazza!"
    
        hotb = HotBeverage()
        coff = Coffee()
        t = Tea()
        choco = Chocolate()
        cappu = Cappuccino()

        print(f"{hotb}\n")
        print(f"{coff}\n")
        print(f"{t}\n")
        print(f"{choco}\n")
        print(cappu)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()