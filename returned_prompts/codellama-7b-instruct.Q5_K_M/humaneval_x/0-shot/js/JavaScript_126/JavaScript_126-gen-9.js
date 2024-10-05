const isSorted = (lst) => {
  // const sorted = lst.every((val, ind) => ind === 0 || val > lst[ind - 1])
  // const noDups = lst.every((val, ind) => lst.indexOf(val) === ind)
  // return sorted && noDups

B:
const isSorted = (lst) => {
  return (lst.every((val, ind) => ind === 0 || val > lst[ind - 1]) &&
          lst.every((val, ind) => lst.indexOf(val) === ind))

C:
const isSorted = (lst) => {
  let isSorted = false
  let noDups = false
  for (let i = 0; i < lst.length; i++) {
    if (i === 0 || lst[i] > lst[i - 1]) {
      isSorted = true
    } else {
      isSorted = false
      break
    }
    if (lst.indexOf(lst[i]) === i) {
      noDups = true
    } else {
      noDups = false
      break
    }
  }
  return isSorted && noDups
}

D:
const isSorted = (lst) => {
  let sorted = false
  let noDups = false
  for (let i = 0; i < lst.length; i++) {
    if (i === 0 || lst[i] > lst[i - 1]) {
      sorted = true
    } else {
      sorted = false
      break
    }
    if (lst.indexOf(lst[i]) === i) {
      noDups = true
    } else {
      noDups = false
      break
    }
  }
  return sorted && noDups
}

E:
const isSorted = (lst) => {
  return lst.every((val, ind) => ind === 0 || val > lst[ind - 1]) &&
         lst.every((val, ind) => lst.indexOf(val) === ind)
}

F:
const isSorted = (lst)