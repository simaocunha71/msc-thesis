  let test2 = test.split(" ")
  let count = {};
  for (let i = 0; i < test2.length; i++) {
    if (count[test2[i]] == undefined) {
      count[test2[i]] = 1
    } else {
      count[test2[i]] += 1
    }
  }
  let max = 0
  let max2 = {}
  for (let key in count) {
    if (count[key] > max) {
      max = count[key]
      max2 = {}
      max2[key] = max
    } else if (count[key] == max) {
      max2[key] = max
    }
  }
  return max2
}


