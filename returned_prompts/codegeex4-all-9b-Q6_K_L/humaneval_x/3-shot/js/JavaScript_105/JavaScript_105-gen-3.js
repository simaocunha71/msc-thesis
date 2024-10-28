  var result = [];
  var names = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  var filtered_arr = arr.filter(x => x >= 1 && x <= 9);
  filtered_arr.sort((a, b) => a - b);
  filtered_arr.reverse();
  for (const n of filtered_arr) {
    result.push(names[n - 1]);
  }
  return result;
}



