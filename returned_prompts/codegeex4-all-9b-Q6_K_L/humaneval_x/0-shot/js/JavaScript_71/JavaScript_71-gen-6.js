```
  let sides = [a,b,c]
  sides.sort((a,b) => a - b)
  let [a1, a2, a3] = sides

  if (a1 + a2 > a3) {
    let s = (a1 + a2 + a3) / 2
    return (Math.sqrt(s * (s - a1) * (s - a2) * (s - a3))).toFixed(2)
  } else {
    return -1
  }
}
```