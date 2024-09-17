def sort_numeric_strings(lst):
    try:
        return sorted(map(int, lst))
    except ValueError:
        return "Error: The list contains non-numeric strings"