def count_words(text: str) -> int:
    return len(text.split())

def count_characters(book_text: str) -> dict:
    counts = {}
    for ch in book_text.lower():
        if 'a' <= ch <= 'z':  # restrict to ASCII letters
            counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_characters(character_dict: dict) -> list[dict]:
    # returns list like [{"char": "e", "num": 10234}, ...] sorted desc by count
    return sorted(
        ({"char": ch, "num": n} for ch, n in character_dict.items()),
        key=lambda item: item["num"],
        reverse=True,
    )
