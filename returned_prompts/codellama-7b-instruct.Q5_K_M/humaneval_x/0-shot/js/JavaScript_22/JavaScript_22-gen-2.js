const filterIntegers = (values) => {
  return values.filter(value => typeof value === 'number' && Number.isInteger(value))
}

B:
const filterIntegers = (values) => {
  return values.filter(value => value % 1 === 0)
}

C:
const filterIntegers = (values) => {
  return values.filter(value => typeof value === 'number' && value === Math.floor(value))
}
