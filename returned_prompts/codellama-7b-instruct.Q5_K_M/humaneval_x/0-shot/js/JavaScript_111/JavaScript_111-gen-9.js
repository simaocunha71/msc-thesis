const histogram = (str) => {
  let res = {};
  let arr = str.split(' ');
  for (let i = 0; i < arr.length; i++) {
    if (res[arr[i]] === undefined) {
      res[arr[i]] = 1;
    } else {
      res[arr[i]]++;
    }
  }
  return res;
};

