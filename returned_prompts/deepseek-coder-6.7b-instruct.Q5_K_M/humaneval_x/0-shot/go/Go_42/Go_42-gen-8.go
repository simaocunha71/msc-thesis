
	for i, v := range l {
		l[i] = v + 1
	}
	return l
}

```


## Go

```go

package main

import "fmt"

func IncrList(l []int) []int {

	for i, v := range l {
		l[i] = v + 1
	}
	return l
}

func main() {

	fmt.Println(IncrList([]int{1, 2, 3})) // 输出 [2, 3, 4]

	fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123})) // 输出 [6, 4, 6, 3, 4, 4, 10, 1, 124]

}

```


## Julia

```julia

# Return list with elements incremented by 1.
function IncrList(l::Array{Int64, 1})
	return l .+ 1
end

println(IncrList([1, 2, 3])) # 输出 [2, 3, 4]

println(IncrList([5, 3, 5, 2, 3, 3, 9, 0, 123])) # 输出 [6, 4, 6, 3, 4, 4, 10, 1, 124]

```


## Kotlin

```kotlin

fun IncrList(l: List<Int>): List<Int> {

    val result = l.map { it + 1 }
    return result
}

fun main(args: Array<String>) {

    println(IncrList(listOf(1, 2, 3))) // 输出 [2, 3, 4]

    println(IncrList(listOf(5, 3, 5, 2, 3, 3, 9, 0, 123))) // 输出 [6, 