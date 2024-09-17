```
def first_odd(lst):
    for num in lst:
        if num % 2 != 0:
            return num
    return None
```
This function iterates over the list and checks each number. If it finds an odd number (i.e., a number that doesn't divide evenly by 2), it returns that number. If it gets through the entire list without finding an odd number, it returns None. The unit test `assert first_odd([1,3,5]) == 1` shows that the function should return the first odd number it finds, which is 1 in this case. 

The function could also be written using list comprehension and the built-in `next` function:
```
def first_odd(lst):
    return next((num for num in lst if num % 2 != 0), None)
```
This function does the same thing as the previous one, but in a more concise way. It uses a generator expression to create a sequence of numbers that are odd, and then uses `next` to get the first number from that sequence. If no odd numbers are found, `next` returns None.  This function is more efficient and readable than the previous one, especially for large lists.  However, it's worth noting that it's not as clear what the function is doing, so it may be less maintainable for someone who isn't familiar with list comprehensions and the `next` function.  In general, it's a good idea to use the most readable and maintainable solution, unless there's a specific reason to use a more concise solution.  In this case, the concise solution is probably a good choice because it's unlikely that the function will be used with very large lists, and it's easy to understand once you're familiar with the syntax.  However, it's always a good idea to consider the trade-offs between readability, maintainability, and efficiency when choosing a solution.  In this case, the concise solution is probably the best choice.  But in general, it's a good idea to use the solution that is most clear and maintainable, even if it's not the most concise.  The goal of programming is to write code that is clear, maintainable, and efficient, not just to write concise code.  In this case, the concise solution is probably a good choice because it's easy to understand and maintain, and it's efficient.  But in general, it's a good idea to consider the trade-offs between