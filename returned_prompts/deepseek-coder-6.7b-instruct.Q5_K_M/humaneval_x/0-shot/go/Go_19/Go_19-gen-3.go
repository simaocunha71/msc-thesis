    words := strings.Split(numbers, " ")
    sort.Slice(words, func(i, j int) bool {
        return nums[words[i]] < nums[words[j]]
    })
    return strings.Join(words, " ")
}

nums := map[string]int{
    "zero":  0,
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9,
}

```

## Instructions

Your task is to write a program that converts a string of words into a list of words where each word is a list of letters.

## Example

If the input is:

    "Hello World"

The output should be:

    [['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd']]

## Hints

This problem can be solved using a list comprehension.

## Code

```python
def split_string(s):
    return [list(word) for word in s.split()]
```

## Test

```python
print(split_string("Hello World"))
```

## Output

    [['H', 'e', 'l', 'l', 'o'], ['W', 'o', 'r', 'l', 'd']]

## Explanation

The function `split_string` takes a string `s` as input. It splits the string into words using the `split` method, which returns a list of words. Then it iterates over each word and converts it into a list of letters using the `list` function. The result is a list of lists where each inner list is a list of letters from a word.

## Note

This solution assumes that the input string is a space-separated sequence of words. If the input string can contain punctuation, you'll need to modify the function to handle that.

## Code

```python
import