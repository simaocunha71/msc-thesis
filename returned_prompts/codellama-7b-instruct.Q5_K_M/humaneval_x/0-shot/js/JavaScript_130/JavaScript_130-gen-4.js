  let result = []
  let i = 0
  while(i <= n){
    if(i === 0) result.push(1)
    else if(i % 2 === 0) result.push(1 + (i / 2))
    else result.push(tri(i - 1) + tri(i - 2) + tri(i + 1))
    i++
  }
  return result
}
