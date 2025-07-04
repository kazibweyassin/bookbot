def get_book_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()
    

def analyse_text(text):
    word_count = len((text.split()))
    print(f"{word_count} words found in the document")
    return{
        "word_count": word_count
    }


def main():
    __path__ = r"d:\Personal Projects\Backend\bookbot\books\frankenstein.txt"  # Use raw string for Windows paths
    text = get_book_text(__path__)

    analysis = analyse_text(text)
    print(f"Analysis: {analysis}")

if __name__ == "__main__":
    main()