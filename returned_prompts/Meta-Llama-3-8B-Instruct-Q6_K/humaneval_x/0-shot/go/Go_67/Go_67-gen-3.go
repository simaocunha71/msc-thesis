Here is the solution in Go:

```go
import (
    "strconv"
    "strings"
)

func FruitDistribution(s string, n int) int {
    // Split the string into two parts: apples and oranges
    parts := strings.Split(s, " and ")
    // Extract the number of apples and oranges from the string
    appleStr := strings.Split(parts[0], " ")[0]
    orangeStr := strings.Split(parts[1], " ")[0]
    // Convert the string to int
    apple, _ := strconv.Atoi(appleStr)
    orange, _ := strconv.Atoi(orangeStr)
    // Calculate the total number of fruits in the basket
    total := n - apple - orange
    return total
}
```


This function splits the input string into two parts, then extracts the numbers of apples and oranges from these parts. It then converts these numbers to integers and calculates the total number of fruits in the basket by subtracting the number of apples and oranges from the total number of fruits. The function returns this total number.