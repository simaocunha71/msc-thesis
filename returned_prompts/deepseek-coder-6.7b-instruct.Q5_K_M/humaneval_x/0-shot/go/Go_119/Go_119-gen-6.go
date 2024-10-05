
// I: ['()(', ')'], O: 'Yes'
// I: [')', ')'], O: 'No'

// The approach is to iterate over each string in the given list,
// and for each string, count the number of open and close parentheses.
// If the total number of open parentheses is greater than the total
// number of close parentheses, we can add the missing number of closed parentheses
// to make the string balanced. If it is not possible to make it balanced,
// return 'No'. If we can make it balanced for all strings, return 'Yes'.

  open := 0
  close := 0

  for _, str := range lst {
    for _, char := range str {
      if string(char) == "(" {
        open++
      } else if string(char) == ")" {
        if open > 0 {
          open--
        } else {
          return "No"
        }
      }
    }
  }

  if open == 0 {
    return "Yes"
  }

  return "No"
}

// Test:

func main() {
  fmt.Println(MatchParens([]string{"()(", ")"})) // 'Yes'
  fmt.Println(MatchParens([]string{")", ")"})) // 'No'
}

// Output:
// Yes
// No

// Explanation:
// In the first example, we can add one open parenthesis to the first string to make it good.
// In the second example, we need two more close parentheses to make the string good.
```

## Tags

#string-manipulation #parentheses-balancing #algorithm-implementation

## Solution

The solution is to iterate through each character in the given strings and count the number of open and close parentheses. If the total number of open parentheses is greater than the total number of close parentheses, we can add the missing number of close parentheses to make the string balanced. If it is not possible to make it balanced, return 'No'. If we can make it balanced for all strings, return 'Yes'.