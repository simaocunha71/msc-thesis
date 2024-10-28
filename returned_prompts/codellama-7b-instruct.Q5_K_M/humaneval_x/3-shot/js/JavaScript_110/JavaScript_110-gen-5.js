  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 == 0) {
      for (let j = 0; j < lst1.length; j++) {
        if (lst1[j] % 2 == 0) {
          [lst1[j], lst2[i]] = [lst2[i], lst1[j]];
          return "YES";
        }
      }
    }
  }
  return "NO";
}



