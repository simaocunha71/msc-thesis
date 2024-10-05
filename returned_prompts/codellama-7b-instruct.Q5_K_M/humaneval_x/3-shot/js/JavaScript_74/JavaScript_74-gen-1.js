numbers = numbers.split()
numbers.sort(key=lambda x: int(x[:-4]))
return ' '.join(numbers)
