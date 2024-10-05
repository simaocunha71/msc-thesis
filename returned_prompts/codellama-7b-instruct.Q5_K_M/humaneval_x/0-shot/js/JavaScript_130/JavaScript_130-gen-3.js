const tri = (n) => {
  const arr = [1, 3]
  for (let i = 2; i <= n; i++) {
    if (i % 2 === 0) {
      arr.push(1 + i / 2)
    } else {
      arr.push(arr[i - 1] + arr[i - 2] + arr[i + 1])
    }
  }
  return arr
}
