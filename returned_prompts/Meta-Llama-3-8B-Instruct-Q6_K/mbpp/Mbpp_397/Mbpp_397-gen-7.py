```
def median_numbers(a, b, c):
    numbers = [a, b, c]
    numbers.sort()
    if len(numbers) % 2 == 0:
        median = (numbers[len(numbers)//2 - 1] + numbers[len(numbers)//2]) / 2
    else:
        median = numbers[len(numbers)//2]
    return median
```


The function takes three numbers as input and returns their median. If the total number of inputs is even, the median is the average of the two middle numbers. If the total number of inputs is odd, the median is the middle number. The function first sorts the input numbers and then calculates the median based on the number of inputs. The unit test `assert median_numbers(25,55,65)==55.0` ensures that the function returns the correct median for the given inputs. 














