const changeBase = (x, base) => {
  const num = x.toString(base)
  return num
}

B:
const changeBase = (x, base) => {
  const num = x.toString(base)
  return num.replace(/1/g, 'a').replace(/0/g, 'b').replace(/2/g, 'c').replace(/3/g, 'd').replace(/4/g, 'e').replace(/5/g, 'f').replace(/6/g, 'g').replace(/7/g, 'h').replace(/8/g, 'i').replace(/9/g, 'j')
}

C:
const changeBase = (x, base) => {
  const num = x.toString(base)
  return num.replace(/[0123456789]/g, (c) => 'a'.repeat(c))
}
