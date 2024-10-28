  return l.sort((a, b) => a - b).some(x => l.includes(0 - x))
}

// 1. sort l in ascending order
// 2. use includes(0 - x) to check if there is an element that is the negation of x
