/* Concatenate list of strings into a single string
  >>> concatenate([])
  ''
  >>> concatenate(['a', 'b', 'c'])
  'abc'
  */
const concatenate = (strings) => {
  return strings.reduce((acc, curr) => acc + curr, '') || '';
};

/* Concatenating list of numbers into one string of comma separated values:
  >>> concatenate([10])
  10
  >>> concatenate([10,20])
  '10,20'
  */
const concatNums = (nums) => {
  let res = '';
  nums.forEach((num) => {
    if (res.length === 0) {
      res += String(num);
    } else {
      res += ',';
      res += String(num);
    }
  });
  return res;
};

/* Concatenate list of lists into a single list */
const concatList = (lists) => {
  const result = [];
  for (let i = 0; i < lists.length; ++i) {
    result.push(...lists[i]);
  }
  return result;
};

/* Concatenate list of objects into a single object */
const concatObj = (objects, keyToConcat) => {
  const result = {};
  for (let i = 0; i < objects.length; ++i) {
    let currItem = objects[i];
    if (!result[currItem[keyToConcat]] && currItem !== null) {
      result[currItem[keyToConcat]] = [];
    }
    result[currItem[keyToConcat]].push(currItem);
  }
  return result;
};