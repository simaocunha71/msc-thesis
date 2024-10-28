def fruit_distribution(s: str, n: int) -> int:
    fruits = s.split(' ')
    total_apples = int(fruits[0])
    total_oranges = int(fruits[4])
    return n - total_apples - total_oranges

