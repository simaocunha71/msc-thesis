  let max_freq = 0;
  let max_num = -1;

  for (let num of lst) {
    if (num > 0) {
      let freq = lst.filter(x => x === num).length;
      if (freq >= num && num > max_freq) {
        max_freq = freq;
        max_num = num;
      }
    }
  }

  return max_num;
}
// Another solution
const search = (lst) => {
  let max_freq = 0;
  let max_num = -1;

  for (let num of lst) {
    if (num > 0) {
      let freq = lst.filter(x => x === num).length;
      if (freq >= num && freq > max_freq) {
        max_freq = freq;
        max_num = num;
      }
    }
  }

  return max_num;
}
// Another solution
const search = (lst) => {
  let max_num = -1;
  for (let num of lst) {
    let freq = lst.filter(x => x === num).length;
    if (num > 0 && freq >= num && freq > max_freq) {
      max_freq = freq;
      max_num = num;
    }
  }

  return max_num;
}
// Another solution
const search = (lst) => {
  let max_num = -1;
  for (let num of lst) {
    if (num > 0) {
      let freq = lst.filter(x => x === num).length;
      if (freq >= num && freq > max_freq) {
        max_freq = freq;
        max_num = num;
      }
    }
  }

  if (max_num === -1) {
    return -1;
  }
  return max_num;
}