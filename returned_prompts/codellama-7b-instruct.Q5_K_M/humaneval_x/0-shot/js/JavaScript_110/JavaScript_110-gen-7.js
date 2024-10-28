/*
  The main idea is to check if all elements of lst1 are even,
  if not, then we have to check if the elements of lst2 are odd,
  if it is, then we can exchange some elements of lst1 and lst2,
  and make all elements of lst1 even.
  */
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 !== 0) {
      if (lst2.every(x => x % 2 === 0)) {
        return "YES";
      }
      return "NO";
    }
  }
  return "YES";
};
