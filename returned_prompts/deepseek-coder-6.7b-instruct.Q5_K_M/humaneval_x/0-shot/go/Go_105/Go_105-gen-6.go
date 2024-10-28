  var (
    output = make([]string, 0)
    names = [10]string{"", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"}
  )

  sort.Ints(arr)

  for i := 0; i < len(arr)/2; i++ {
    arr[i], arr[len(arr)-i-1] = arr[len(arr)-i-1], arr[i]
  }

  for _, num := range arr {
    if num >= 1 && num <= 9 {
      output = append(output, names[num])
    }
  }

  return output
}


