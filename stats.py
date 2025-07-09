def analyse_text(text):
    word_count = len((text.split()))
    print(f"{word_count} words found in the document")
    return{
        "word_count": word_count
    }
