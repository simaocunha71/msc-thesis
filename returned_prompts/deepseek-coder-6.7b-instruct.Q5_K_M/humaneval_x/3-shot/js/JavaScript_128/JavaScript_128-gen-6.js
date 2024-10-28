  if(arr.length == 0) return null

  let sum = 0
  let prod = 1

  for(let i = 0; i < arr.length; i++){
    if(arr[i] > 0) {
      sum += Math.abs(arr[i])
      prod *= 1
    } else if (arr[i] < 0) {
      sum += Math.abs(arr[i])
      prod *= -1
    } else {
      return 0
    }
  }

  return prod * sum
}



