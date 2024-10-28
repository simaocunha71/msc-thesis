const antiShuffle = (s) => {
  let newStr = ''
  let arr = s.split(' ')
  for (let i = 0; i < arr.length; i++) {
    let arr2 = arr[i].split('')
    arr2.sort()
    newStr += arr2.join('') + ' '
  }
  return newStr
}
