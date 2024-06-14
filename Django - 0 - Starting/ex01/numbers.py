def main():
    try:
        with open('numbers.txt', 'r') as file:
            content = file.read()
            content = content.replace(',', '\n')
            print(content)
    except FileNotFoundError:
        print("numbers.txt not found")
if __name__ == "__main__":
    main()