const antiShuffle = (s) => {
  let newStr = ''
  let words = s.split(' ')
  for (let i = 0; i < words.length; i++) {
    let sorted = words[i].split('').sort((a, b) => {
      if (a.charCodeAt(0) > b.charCodeAt(0)) {
        return 1
      } else {
        return -1
      }
    }).join('')
    newStr += sorted + ' '
  }
  return newStr.trim()
}