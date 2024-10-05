  for (let num of lst1) {
    if (num % 2 !== 0) {
      for (let num2 of lst2) {
        if (num2 % 2 === 0) {
          return "YES";
        }
      }
      return "NO";
    }
  }
  return "YES";
}...



