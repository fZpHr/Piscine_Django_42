from local_lib.path import Path

def main():
    try:
        path = Path(__file__).parent / "test"
        if not path.exists():
            path.mkdir()
        new_path = path / "test.txt"
        new_path.write_text("Hello, World!")
        print(new_path.read_text())
    except Exception as e: 
        print(e)

if __name__ == '__main__' :
    main() 