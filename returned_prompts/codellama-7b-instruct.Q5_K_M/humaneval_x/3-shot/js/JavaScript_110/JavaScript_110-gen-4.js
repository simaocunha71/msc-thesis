  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 == 1) {
      for (let j = 0; j < lst2.length; j++) {
        if (lst2[j] % 2 == 0) {
          let tmp = lst1[i];
          lst1[i] = lst2[j];
          lst2[j] = tmp;
          return "YES";
        }
      }
    }
  }
  return "NO";
}



