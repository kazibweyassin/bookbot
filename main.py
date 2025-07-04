def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    path = r"d:\Personal Projects\Backend\bookbot\books\frankenstein.txt" 
    text = get_book_text(path)
    print(text)

if __name__ == "__main__":
    main()