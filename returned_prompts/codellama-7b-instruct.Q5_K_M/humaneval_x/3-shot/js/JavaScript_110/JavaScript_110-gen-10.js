  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 == 0) {
      for (let j = 0; j < lst1.length; j++) {
        if (lst1[j] % 2 != 0) {
          let temp = lst1[j];
          lst1[j] = lst2[i];
          lst2[i] = temp;
          if (lst1.every(x => x % 2 == 0)) {
            return "YES";
          }
        }
      }
    }
  }
  return "NO";
}



