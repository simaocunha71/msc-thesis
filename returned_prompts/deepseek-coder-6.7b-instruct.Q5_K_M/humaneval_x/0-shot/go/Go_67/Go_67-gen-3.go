	apples := strings.Fields(s)[0]
	oranges := strings.Fields(s)[4]
	appleInt, _ := strconv.Atoi(apples)
	orangeInt, _ := strconv.Atoi(oranges)

B:
	return n - appleInt - orangeInt
}

// The code above is a function that takes a string and an integer as arguments. 
// The string is split into words to extract the number of apples and oranges. 
// These numbers are converted from string to integer. 
// Finally, it calculates the number of mangoes by subtracting the number of apples and oranges from the total number of fruits. 
// It returns the result.


// The function FruitDistribution is incomplete, it doesn't handle the case where the string could contain more than one digit for the number of fruits.
// The function FruitDistribution does not handle the case where the string could contain more than one digit for the number of fruits.
// For example, FruitDistribution("10 apples and 6 oranges",20) should return 14, but the current function will return 10.
// To fix this, you should update the function to handle multi-digit numbers correctly.

// Hint:
// You can use the strconv.Atoi function to convert a string to an integer in Go.
// The strings.Fields function splits a string into words.
// The [] operator can be used to access the elements of an array or slice.
// The + operator can be used to add two integers.
// The - operator can be used to subtract one integer from another.

// Test Cases:
// FruitDistribution("5 apples and 6 oranges", 19) ->19  - 5  - 6  =  8
// FruitDistribution("0 apples and 1 oranges",3) -> 3 - 0 - 1 = 2
// FruitDistribution("2 apples and 3 oranges", 100) -> 100 - 2 - 3 = 95
// FruitDistribution("100 apples and 1 oranges",120) -> 120 - 100