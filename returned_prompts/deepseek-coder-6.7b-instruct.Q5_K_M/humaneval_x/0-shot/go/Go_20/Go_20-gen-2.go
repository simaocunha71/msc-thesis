
    sort.Float64s(numbers)
    minDiff := math.MaxFloat64
    result := [2]float64{}

    for i := 0; i < len(numbers)-1; i++ {
        if diff := numbers[i+1] - numbers[i]; diff < minDiff {
            result[0], result[1] = numbers[i], numbers[i+1]
            minDiff = diff
        }
    }

    return result
}

```


{{out}}

```txt

FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) = [2.0, 2.2]
FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) = [2.0, 2.0]

```



## Julia


```julia
function FindClosestElements(numbers)
    numbers = sort(numbers)
    min_diff = Inf
    result = []

    for i = 1:(length(numbers) - 1)
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff
            result = [numbers[i], numbers[i+1]]
            min_diff = diff
        end
    end

    return Tuple(result)
end
```


{{out}}

```txt

julia> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
(2.0, 2.2)

julia> FindClosestElements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
(2.0, 2.0)

```



## Kotlin


```scala
fun findClosestElements(numbers: List<Double>): Pair<Double, Double> {