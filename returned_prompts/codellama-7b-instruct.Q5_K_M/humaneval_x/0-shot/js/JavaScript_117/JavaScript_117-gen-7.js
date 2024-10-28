/*
  const selectWords = (s, n) => {
    if (!s) return []
    const words = s.split(" ")
    return words.filter(w => w.replace(/[aeiou]/g, '').length === n)
  }
  */

B:
/*
const selectWords = (s, n) => {
  if (!s) return []
  const words = s.split(" ")
  return words.filter(w => w.replace(/[aeiou]/g, '').length === n)
}
*/

C:
/*
const selectWords = (s, n) => {
  if (!s) return []
  const words = s.split(" ")
  const consonants = /[^aeiou]/g
  return words.filter(w => w.match(consonants).length === n)
}
*/

D:
/*
const selectWords = (s, n) => {
  if (!s) return []
  const words = s.split(" ")
  const consonants = /[^aeiou]/g
  return words.filter(w => w.match(consonants).length === n)
}
*/

E:
/*
const selectWords = (s, n) => {
  if (!s) return []
  const words = s.split(" ")
  const consonants = /[^aeiou]/g
  return words.filter(w => w.match(consonants).length === n)
}
*/

F:
/*
const selectWords = (s, n) => {
  if (!s) return []
  const words = s.split(" ")
  const consonants = /[^aeiou]/g
  return words.filter(w => w.match(consonants).length === n)
}
*/

G:
/*
const selectWords = (s, n) => {
  if (!s) return []
  const words = s.split(" ")
  const consonants = /[^aeiou]/g
  return words.filter(w => w.match(consonants).length === n)
}
*/