  var names = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
  var result = [];

  for(let number of arr) {
    if(number >= 1 && number <= 9) {
      result.push(names[number]);
    }
  }

  return result.sort().reverse();
}



