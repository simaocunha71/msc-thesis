
def surfacearea_sphere(radius):
    return 4 * math.pi * radius ** 2

print(math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001))
<jupyter_output>
True
<jupyter_text>
3. Create a function that takes a list of numbers, and returns a list with the same length, where each value is the average of the relevant two numbers.Example: average_two_numbers([1, 2, 3, 4, 5]) ➞ [1.5, 2.5, 3.5, 4.5]
<jupyter_code>
def average_two_numbers(lst):
    return [(lst[i] + lst[i + 1]) / 2 for i in range(len(lst) - 1)]

print(average_two_numbers([1, 2, 3, 4, 5]))
<jupyter_output>
[1.5, 2.5, 3.5, 4.5]
<jupyter_text>
4. Create a function that takes a string and returns a string where all the vowels are removed.Example: remove_vowels('Hello, World') ➞ 'Hll, Wrld'
<jupyter_code>
def remove_vowels(txt):
    return ''.join([char for char in txt if char.lower() not in 'aeiou'])

print(remove_vowels('Hello, World'))
<jupyter_output>
Hll, Wrld
<jupyter_text>
5. Create a function that takes a string and returns the number of vowels in it.Example: count_vowels('Hello, World') ➞ 3
<jupyter_code>
def count_vowels(txt):
    return sum(1 for char in txt if char.lower() in 'aeiou')

print(count_vowels('Hello, World