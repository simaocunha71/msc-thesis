from collections import Counter
def sort_counter(counter: dict) -> list:
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)