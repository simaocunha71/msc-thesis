/*Return sorted unique elements in a list
  >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
  [0, 2, 3, 5, 9, 123]
  */
const unique = (l) => {
  const isNumber = (n) => typeof n === 'number';
  l.sort((a, b) => a < b ? -1 : a > b ? 1 : 0); // sort array by value

  let i = 0;
  while(i < l.length && isNumber(l[i])) {
    if(!(isNumber(l[i]))) break;
    i++;
  }

  return l.slice(0, i);
}