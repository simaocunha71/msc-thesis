  let result = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 == 0) {
      result += Math.pow(lst[i], 2);
    } else if (i % 4 == 0) {
      result += Math.pow(lst[i], 3);
    }
  }
  return result;
}



