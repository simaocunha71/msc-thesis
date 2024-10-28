    if strings.Count(file_name, ".") != 1 {
        return "No"
    }
    parts := strings.Split(file_name, ".")
    if len(parts[0]) == 0 || len(parts) != 2 || len(parts[1]) != 3 || (parts[1] != "txt" && parts[1] != "exe" && parts[1] != "dll") {
        return "No"
    }
    count := 0
    for _, c := range parts[0] {
        if '0' <= c && c <= '9' {
            count += 1
        }
    }
    if count > 3 {
        return "No"
    }
    return "Yes"
}
```

## 3.2.7. Solution

```go
import  (
	"fmt"
	"strings"
	"unicode"
	"regexp"
	"math"
)

func main()  {
	fmt.Println(HasCloseElements([]float64{1.0, 2.0, 3.0}, 0.5)) // false
	fmt.Println(HasCloseElements([]float64{1.0, 2.8, 3.0, 4.0, 5.0, 2.0}, 0.3)) // true
	fmt.Println(SeparateParenGroups("(  )  (( ))  (( )( ))")) // ['()', '(())', '(()())']
	fmt.Println(TruncateNumber(3.5)) // 0.5
	fmt.Println(FileNameCheck("example.txt")) // Yes
	fmt.Println(FileNameCheck("1example.dll")) // No
}

func HasCloseElements(numbers  []float64, threshold float64) bool  {
	for i  := 0; i < len(numbers); i++  {
		for j  := i + 1; j < len(numbers); j++  {
			var distance float64 = math.Abs(numbers[i] - numbers[j])
			if distance < threshold