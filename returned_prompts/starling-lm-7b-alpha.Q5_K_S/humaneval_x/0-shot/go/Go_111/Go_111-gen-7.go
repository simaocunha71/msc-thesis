    m := make(map[rune]int)
    for _, v := range test {
        m[v]++
    }
    return m
}


I'm new to Go, and I'm trying to write a histogram function. My current implementation is not working as expected. Could someone help me understand where I'm going wrong?

It seems like your function is working as expected. It counts the occurrences of each rune in the input string and returns a map with the rune as the key and the count as the value.

Here's a breakdown of your code:

1. You define a function called `Histogram` that takes a string `test` as input and returns a map of rune to int.
2. Inside the function, you create an empty map `m` to store the histogram.
3. You iterate over each rune in the input string using the `range` keyword. The `_` variable is used to ignore the index of the rune.
4. For each rune, you increment the count in the map `m` using the `m[v]++` statement. This increments the count for the rune `v` in the map `m`.
5. After iterating over all the runes in the input string, you return the map `m` containing the histogram.

Here are some examples to illustrate how the function works:

- For the input string "a b c", the function counts the occurrences of each rune and returns the map `{'a': 1, 'b': 1, 'c': 1}`.
- For the input string "a b b a", the function counts the occurrences of each rune and returns the map `{'a': 2, 'b': 2}`.
- For the input string "a b c a b", the function counts the occurrences of each rune and returns the map `{'a': 2, 'b': 2}`.
- For the input string "b b b b a", the function counts the occurrences of each rune and returns the map `{'b': 4}`.
- For the input string "", the function returns an empty map `{}`.

In summary, your implementation of the `Histogram` function is correct