To solve this problem we need to perform the following steps:

1. Remove all characters in s that are equal to any character in c.
2. Check if the result string is palindrome.

Here's how we can do that:

1. Create a variable called "result" and set it equal to the string s.
2. Iterate over each character in c and use the replace() method to remove all occurrences of that character from result.
3. Check if the result string is palindrome by comparing it to its reverse. If they are the same, it's a palindrome.
4. Return the result string and whether it's a palindrome as a tuple.

Here's the implementation in JavaScript:

```javascript
function reverseDelete(s, c) {
    let result = s;

    for (let char of c) {
        result = result.replace(new RegExp(char, 'g'), '');
    }

    return [result, result === result.split('').reverse().join('')];
}
```

You can use this function like this:

```javascript
console.log(reverseDelete("abcde", "ae")); // Output: ('bcd', false)
console.log(reverseDelete("abcdef", "b")); // Output: ('acdef', false)
console.log(reverseDelete("abcdedcba", "ab")); // Output: ('cdedc', true)
```

This function will return a tuple containing the result string and whether it's a palindrome.

*/

```python
def reverseDelete(s, c):
    result = s
    for char in c:
        result = result.replace(char, '')
    return (result, result == result[::-1])
```

You can use this function like this:

```python
print(reverseDelete("abcde", "ae"))  # Output: ('bcd', False)
print(reverseDelete("abcdef", "b"))  # Output: ('acdef', False)
print(reverseDelete("abcdedcba", "ab"))  # Output: ('cdedc', True)
```

This function will return a tuple containing