
const exchange = (lst1, lst2) => {
  let even = true;
  for (let i = 0; i < lst1.length; i++) {
    if (lst1[i] % 2 != 0) {
      even = false;
      break;
    }
  }
  if (even) return "YES";
  for (let i = 0; i < lst1.length; i++) {
    for (let j = 0; j < lst2.length; j++) {
      if (lst1[i] == lst2[j]) {
        lst2.splice(j, 1);
        break;
      }
    }
  }
  if (lst2.length == 0) return "YES";
  return "NO";
};
