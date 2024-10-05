  const names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  let result = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] >= 1 && arr[i] <= 9) {
      result.push(names[arr[i] - 1]);
    }
  }
  return result.reverse();
}