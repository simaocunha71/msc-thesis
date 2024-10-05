  let count_map 

  for (let i = lst.length - 1; i >= 0; i--) {
    if ((count_map === undefined) || (count_map[lst[i]] === undefined)) {
      count_map = {}
      for (let j = 0; j < lst.length; j++) {
        if (lst[j] in count_map) {
          count_map[lst[j]] += 1
        } else {
          count_map[lst[j]] = 1
        }
      }
      if ((lst[i] in count_map) && (count_map[lst[i]] >= lst[i])) {
        return lst[i]
      }
    }
  }
  return -1
}



