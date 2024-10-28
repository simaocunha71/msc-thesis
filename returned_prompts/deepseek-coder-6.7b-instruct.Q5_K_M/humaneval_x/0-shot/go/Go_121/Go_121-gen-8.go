
sum := 0

for i, v := range lst {

	if i%2 == 0 && v%2 != 0 {
		sum += v
	}
}

return sum

}

func main() {

	fmt.Println(Solution([]int{5, 8, 7, 1})) // 12
	fmt.Println(Solution([]int{3, 3, 3, 3, 3})) // 9
	fmt.Println(Solution([]int{30, 13, 24, 321})) // 0
}

// The code sums all the odd integers at even indexes in the list.
```

</div>

<div class="mt-8">

## Problem 2: Sum of Even Indexed Elements

