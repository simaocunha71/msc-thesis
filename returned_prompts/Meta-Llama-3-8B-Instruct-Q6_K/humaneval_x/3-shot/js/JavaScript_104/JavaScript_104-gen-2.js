  return x.filter(num => !/\d/.test(String(num).replace(/2|4|6|8/g, ''))).sort((a, b) => a - b);
}
// or
const uniqueDigits = (x) => {
  return x.filter(num => !/(2|4|6|8)/.test(String(num))).sort((a, b) => a - b);
}
// or
const uniqueDigits = (x) => {
  return x.filter(num => !~String(num).indexOf('2') && !~String(num).indexOf('4') && !~String(num).indexOf('6') && !~String(num).indexOf('8')).sort((a, b) => a - b);
}
// or
const uniqueDigits = (x) => {
  return x.filter(num => !~[2,4,6,8].some(digit => String(num).includes(digit))).sort((a, b) => a - b);
}  // more readable
// or
const uniqueDigits = (x) => {
  return x.filter(num => !~[...String(num)].map(Number).filter(digit => [2,4,6,8].includes(digit)).join('')).sort((a, b) => a - b);
}
// or
const uniqueDigits = (x) => {
  return x.filter(num => !String(num).replace(/1|3|5|7|9/g, '').length).sort((a, b) => a - b);
}  // most efficient
// or
const uniqueDigits = (x) => {
  return x.filter(num => !~[...String(num)].map(Number).filter(digit => digit % 2 == 0).join('')).sort((a, b) => a - b);
}
// or
const uniqueDigits = (x) => {
  return x.filter(num => !~String(num).replace(/1|3|5|7|9/g, '').length).sort((a, b) => a - b);
}
// or
const uniqueDigits = (x) => {
  return x.filter(num => !~[...String(num)].map(Number).filter(digit => digit % 2 == 0).join('')).sort((a, b) => a - b);
}
// or
const uniqueDigits = (x) => {
  return x.filter(num => !~[...String(num)].map