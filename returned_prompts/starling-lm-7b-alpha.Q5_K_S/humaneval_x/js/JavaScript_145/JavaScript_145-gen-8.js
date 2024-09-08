  const map = {
    -1: -2,
    0: -1,
    -2: -1
  }

  return nums
    .map(num => [num, num + '', ...num.toString().split('').map(c => map[c]), num])
    .sort()
    .map(item => item[1])
}



