  let count = {}

  for (let i = 0; i < lst.length; i++) {
    if (lst[i] in count) {
      count[lst[i]] += 1
    } else {
      count[lst[i]] = 1
    }
  }

  for (let key in count) {
    if (count[key] >= +key) {
      return +key
    }
  }
  return -1
}



