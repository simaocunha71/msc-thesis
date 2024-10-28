  let arr = test.split(" ");
  let dict = {};
  let max = 0;
  for (let i = 0; i < arr.length; i++) {
    if (dict[arr[i]] == undefined) {
      dict[arr[i]] = 1;
    } else {
      dict[arr[i]]++;
    }
  }

  for (let key in dict) {
    if (dict[key] > max) {
      max = dict[key];
    }
  }
  for (let key in dict) {
    if (dict[key] == max) {
      delete dict[key];
    }
  }

  return dict;
}



