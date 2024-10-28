  if (numbers.length == 0) {
    return [];
  }
  var result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    result.push(delimeter);
    result.push(numbers[i]);
  }
  return result;
}  // or
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, current, index) => {
    if (index > 0) {
      acc.push(delimeter);
    }
    acc.push(current);
    return acc;
  }, []);
}  // or
const intersperse = (numbers, delimeter) => {
  return [numbers[0]].concat(...numbers.slice(1).map(x => [delimeter, x]));
}  // or
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, current, index) => {
    if (index > 0) {
      acc.push(delimeter);
    }
    acc.push(current);
    return acc;
  }, []).join('');
}  // or
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, current, index) => {
    if (index > 0) {
      acc += delimeter;
    }
    acc += current;
    return acc;
  }, '');
}  // or
const intersperse = (numbers, delimeter) => {
  return numbers.slice(0, -1).reduce((acc, current, index) => {
    acc.push(current);
    acc.push(delimeter);
    return acc;
  }, []).concat([numbers[numbers.length - 1]]);
}  // or
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, current, index) => {
    if (index > 0) {
      acc.push(delimeter);
    }
    acc.push(current);
    return acc;
  }, []).slice(0, -1);
}  // or
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, current, index) => {
    if (index > 0) {
      acc.push(delimeter);
    }
    acc.push(current);
    return acc;
  }, []).slice(0, -1).concat([numbers[numbers.length - 1]]);
}  // or
const intersperse = (numbers, delimeter) => {
  return numbers.reduce((acc, current, index