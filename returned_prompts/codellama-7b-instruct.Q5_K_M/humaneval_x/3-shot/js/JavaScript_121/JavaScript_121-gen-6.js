  let result = 0;
  let odd_positions = [];

  for (let i = 0; i < lst.length; i++) {
    if (i % 2 != 0 && lst[i] % 2 != 0) {
      odd_positions.push(lst[i]);
    }
  }

  for (let i = 0; i < odd_positions.length; i++) {
    result += odd_positions[i];
  }

  return result;
}



