  var even_nums = [];
  for (const num of lst1) {
    if (num % 2 == 0) {
      even_nums.push(num);
    }
  }

  if (even_nums.length == lst1.length) {
    return "YES";
  }

  for (const num of lst2) {
    if (num % 2 == 0) {
      even_nums.push(num);
    }
  }

  if (even_nums.length == lst1.length) {
    return "YES";
  }

  return "NO";
}



