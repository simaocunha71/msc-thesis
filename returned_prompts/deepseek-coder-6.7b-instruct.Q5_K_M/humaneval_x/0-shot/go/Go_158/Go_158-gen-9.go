    sort.Strings(words)

B:
    max := -1
    maxWord := ""

C:
    for _, word := range words {

D:
        unique := make(map[rune]struct{})

E:
        for _, char := range word {
            unique[char] = struct{}{}
        }

F:
        if len(unique) > max {
            max = len(unique)
            maxWord = word
        }
    }

G:
    return maxWord
}

// What are the time and space complexity of the above code?
// Time complexity: O(n * m)
// Space complexity: O(n)

// What is the time complexity of sort.Strings() function?
// Time complexity: O(n log n)

// How does the time complexity of the final solution compare to the sum of time complexities of sort.Strings() and the for loop?
// Time complexity: O(n * m) + O(n log n) = O(n log n) + O(n * m) = O(n * m)
```

## Solution
```go
import (
	"sort"
)

func FindMax(words []string) string {

	sort.Strings(words)

	max := -1
	maxWord := ""

	for _, word := range words {
		unique := make(map[rune]struct{})
		for _, char := range word {
			unique[char] = struct{}{}
		}
		if len(unique) > max {
			max = len(unique)
			maxWord = word
		}
	}

	return maxWord
}
```

## Explanation

The function `FindMax` takes as input a slice of strings `words`. The strings are sorted in lexicographical order.

Then, it iterates through the sorted list of words. For each word, a map `unique` is created that stores unique characters of the word. The length of the map is then compared to `max`. If the length of the map is greater than `max`, `max` is updated and `maxWord