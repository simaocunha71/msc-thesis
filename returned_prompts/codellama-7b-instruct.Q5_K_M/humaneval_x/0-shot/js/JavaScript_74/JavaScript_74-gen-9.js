const totalMatch = (lst1, lst2) => {
  let minLength = lst1.length;

  if (lst2.length < minLength) {
    minLength = lst2.length;
  }

  for (let i = 0; i < minLength; i++) {
    if (lst1[i].length > lst2[i].length) {
      return lst2;
    }
  }
  return lst1;
};









