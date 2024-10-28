  let total_eaten 
  let left_over
  if (remaining >= need) {
    total_eaten = number + need
    left_over = 0
  } else {
    total_eaten = number + remaining
    left_over = need - remaining
  }
  return [total_eaten, left_over]
}



