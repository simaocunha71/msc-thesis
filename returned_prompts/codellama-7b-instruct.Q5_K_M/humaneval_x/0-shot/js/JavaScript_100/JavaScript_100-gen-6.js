const makeAPile = n => Array.from(
  { length: n },
  (_, i) => i % 2 === 0 ? n + (i + 1) * 2 : n + (i + 1) * 2 + 1
)

  // let i = 0
  // const arr = []
  // while (i < n) {
  //   const next = i % 2 === 0 ? n + (i + 1) * 2 : n + (i + 1) * 2 + 1
  //   arr.push(next)
  //   i = next
  // }

  // return arr
}



// 