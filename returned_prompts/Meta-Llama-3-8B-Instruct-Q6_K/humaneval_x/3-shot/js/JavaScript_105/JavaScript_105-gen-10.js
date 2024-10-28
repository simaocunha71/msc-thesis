  let result = [];
  arr.sort((a, b) => a - b).reverse();
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      result.push(names[arr[i]]);
    }
  }
  return result;

  let names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
}