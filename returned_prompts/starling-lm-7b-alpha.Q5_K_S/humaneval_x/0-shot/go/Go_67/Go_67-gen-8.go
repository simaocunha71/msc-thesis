	arr := strings.Split(s, " ")
	var total int
	for _, v := range arr {
		if v[0] == 'a' {
			num, _ := strconv.Atoi(strings.Trim(v, " apples"))
			total += num
		} else {
			num, _ := strconv.Atoi(strings.Trim(v, " oranges"))
			total += num
		}
	}
	return n - total
}

Answer:3

Explanation:

The total number of mangos is equal to the total number of fruits in the basket minus
the number of apples and oranges.

To find the number of apples and oranges, we can iterate through the given string and count
the number of apples and oranges. In this case, we can use the split function to split the
string into an array of strings. Then, we can iterate through the array and check if the
first character of each string is "a" or "o". If it is, we can use the trim function to remove
the " apples" or " oranges" from the string and convert the remaining string to an integer.
Finally, we can add up the numbers to get the total number of apples and oranges.

The total number of mangos is then equal to the total number of fruits in the basket minus
the total number of apples and oranges. In this case, it is equal to 19 - 5 - 6 = 8.

In the provided solution, the FruitDistribution function takes a string and an integer as input.
It splits the string into an array of strings using the split function. Then, it initializes a variable called
total to 0. It then iterates through the array and checks if the first character of each string is "a" or "o".
If it is, it uses the trim function to remove the " apples" or " oranges" from the string and converts the remaining
string to an integer using the atoi function. It adds up the numbers to get the total number of apples and oranges.
Finally, it subtracts the total number of apples and or