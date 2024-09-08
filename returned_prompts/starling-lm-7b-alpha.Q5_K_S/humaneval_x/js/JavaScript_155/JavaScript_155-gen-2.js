  let result = [0, 0];
  let num_str = num.toString();

  for (let i = 0; i < num_str.length; i++) {
    if (num_str[i] % 2 == 0) {
      result[0] += 1;
    } else {
      result[1] += 1;
    }
  }

  return result;
}



