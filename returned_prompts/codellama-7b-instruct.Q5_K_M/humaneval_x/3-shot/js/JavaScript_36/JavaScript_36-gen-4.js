  var count = 0;
  for (let i = 11; i < n; i++) {
    if (i % 11 == 0 || i % 13 == 0) {
      let num_str = i.toString();
      for (let j = 0; j < num_str.length; j++) {
        if (num_str[j] == '7') {
          count += 1;
        }
      }
    }
  }

  return count;
}



