  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 == 1 && lst2[i] % 2 == 0) {
      var temp = lst1[i];
      lst1[i] = lst2[i];
      lst2[i] = temp;
    }
  }

  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 == 1) {
      return "NO";
    }
  }

  return "YES";
}



