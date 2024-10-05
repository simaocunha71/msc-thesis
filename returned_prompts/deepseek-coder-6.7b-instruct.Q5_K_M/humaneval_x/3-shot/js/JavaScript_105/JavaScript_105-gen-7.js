  const names = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  let newArr = [];

  arr.sort((a, b) => a - b).reverse();

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      newArr.push(names[arr[i]]);
    }
  }
  return newArr;
}



