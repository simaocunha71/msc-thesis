
	result := make([]int, 0)

	for i, num := range numbers {
		result = append(result, num)
		if i < len(numbers) - 1 {
			result = append(result, delimeter)
		}
	}

	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4)) // []
	fmt.Println(Intersperse([]int{1, 2, 3}, 4)) // [1, 4, 2, 4, 3]
}

```



## Julia


```julia
function intersperse(numbers::Array{Int64, 1}, delimeter::Int64)
    n = length(numbers)
    if n == 0
        return []
    end
    result = Array{Int64, 1}(n+(n-1)*1)
    result[1] = numbers[1]
    j = 2
    for i = 2:n
        result[j] = delimeter
        j += 1
        result[j] = numbers[i]
        j += 1
    end
    return result
end

println(intersperse([], 4))  # []
println(intersperse([1, 2, 3], 4))  # [1, 4, 2, 4, 3]
```



## Kotlin


```kotlin
fun intersperse(numbers: List<Int>, delimiter: Int): List<Int> {
    val result = mutableListOf<Int>()
    numbers.forEachIndexed { index, num ->
        result.add(num)
        if (index < numbers.lastIndex) {
            result.add(delimiter)
        }
    }
    return result
}

fun main(args: Array<String>) {
    println(intersperse(listOf(), 4))  // []
    println(intersperse(listOf(1, 2, 3), 4)) 