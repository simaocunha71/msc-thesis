  for (let i = 0; i < lst2.length; i++) {
    if (lst2[i] % 2 == 0) {
      if (lst1.includes(lst2[i])) {
        const index = lst1.indexOf(lst2[i]);
        lst1[index] = lst2[i];
        return "YES";
      } else {
        lst1.push(lst2[i]);
        return "YES";
      }
    }
  }
  return "NO";
}



