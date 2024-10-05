  if len(array) == 0 {
    return []int{}
  }

  if len(array) == 1 {
    return []int{array[0]}
  }

  var result []int
  sum := array[0] + array[len(array)-1]

  if sum%2 == 0 {
    result = append(result, array...)
    sort.Slice(result, func(i, j int) bool {
      return result[i] > result[j]
    })
  } else {
    result = append(result, array...)
    sort.Ints(result)
  }

  return result
}


