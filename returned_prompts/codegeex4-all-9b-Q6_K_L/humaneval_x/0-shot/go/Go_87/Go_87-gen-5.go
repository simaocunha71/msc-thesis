```go
import (
	"sort"
)

func GetRow(lst [][]int, x int) [][2]int {
	var result [][2]int
	for i, row := range lst {
		for j, val := range row {
			if val == x {
				result = append(result, [2]int{i, j})
			}
		}
	}

	sort.Slice(result, func(i, j int) bool {
		if result[i][0] == result[j][0] {
			return result[i][1] > result[j][1]
		}
		return result[i][0] < result[j][0]
	})

	return result
}
```

B:
```go
import (
	"sort"
)

func GetRow(lst [][]int, x int) [][2]int {
	var result [][2]int
	for i, row := range lst {
		for j, val := range row {
			if val == x {
				result = append(result, [2]int{i, j})
			}
		}
	}

	sort.Slice(result, func(i, j int) bool {
		if result[i][0] == result[j][0] {
			return result[i][1] < result[j][1]
		}
		return result[i][0] < result[j][0]
	})

	return result
}
```

C:
```go
import (
	"sort"
)

func GetRow(lst [][]int, x int) [][2]int {
	var result [][2]int
	for i, row := range lst {
		for j, val := range row {
			if val == x {
				result = append(result, [2]int{i, j})
			}
		}
	}

	sort.Slice(result, func(i, j int) bool {
		if result[i][0] == result[j][0] {
			return result[i][1] > result[j][1]
		}
		return result[i][0] > result[j][0]
	})

	return result
}
```

D:
```go
import (
	"sort"
)

func GetRow(lst [][]int, x int) [][2]int {
	var result [][2]int
	for i, row := range lst {
		for j, val := range row {
			if val == x {
				result = append(result, [2]int{i, j})
			}
		}
	}

	sort.Slice(result, func(i, j int) bool {
	