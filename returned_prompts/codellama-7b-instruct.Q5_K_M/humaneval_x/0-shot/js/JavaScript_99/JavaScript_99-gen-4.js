const closestInteger = (value) => Math.round(value)

B:
const closestInteger = (value) => {
  const number = parseFloat(value)
  return Math.round(number)
}

C:
const closestInteger = (value) => {
  let number = parseFloat(value)
  number = Math.abs(number)
  number = Math.round(number)
  if (number === 0) return 0
  number = number / Math.abs(number)
  return number * Math.round(Math.abs(number))
}

D:
const closestInteger = (value) => {
  let number = parseFloat(value)
  if (number > 0) {
    return Math.ceil(number)
  } else {
    return Math.floor(number)
  }
}

E:
const closestInteger = (value) => {
  const number = parseFloat(value)
  const rounded = Math.round(number)
  if (Math.abs(number - rounded) === 0.5) {
    return number > 0 ? rounded + 1 : rounded - 1
  }
  return rounded
}

F:
const closestInteger = (value) => {
  const number = parseFloat(value)
  const rounded = Math.round(number)
  if (Math.abs(number - rounded) === 0.5) {
    return number > 0 ? rounded + 1 : rounded - 1
  }
  return rounded
}

G:
const closestInteger = (value) => {
  const number = parseFloat(value)
  const rounded = Math.round(number)
  if (Math.abs(number - rounded) === 0.5) {
    return number > 0 ? rounded + 1 : rounded - 1
  }
  return rounded
}

H:
const closestInteger = (value) => {
  const number = parseFloat(value)
  const rounded = Math.round(number)
  if (Math.abs(number - rounded) === 0.5) {
    return number > 0 ? rounded + 1 : rounded - 1
  }
 