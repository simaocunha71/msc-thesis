const strlen = (string) => string.length

B:
const strlen = (string) => {
  let length = 0
  for (let i = 0; i < string.length; i++) {
    if (string[i] !== ' ') length++
  }
  return length
}

C:
const strlen = (string) => {
  let length = 0
  string.split('').forEach((char) => {
    if (char !== ' ') length++
  })
  return length
}

D:
const strlen = (string) => string.split('').filter((char) => char !== ' ').length

E:
const strlen = (string) => string.replace(/ /g, '').length

F:
const strlen = (string) => string.trim().length
