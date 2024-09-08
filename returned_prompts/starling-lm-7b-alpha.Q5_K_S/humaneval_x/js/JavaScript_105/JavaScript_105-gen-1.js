  let result = [];
  for (const i of arr) {
    if (i >= 1 && i <= 9) {
      result.push(num_to_name[i]);
    }
  }
  return result.sort().reverse();
}



