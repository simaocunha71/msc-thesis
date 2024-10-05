    def count_distinct_characters(string: str) -> int:
        return len(set(string.lower()))
    # The set data structure automatically removes duplicates.
    # We convert the string to lowercase to ensure the case-insensitive comparison.
    # Finally, we use the length of the set as the number of distinct characters.