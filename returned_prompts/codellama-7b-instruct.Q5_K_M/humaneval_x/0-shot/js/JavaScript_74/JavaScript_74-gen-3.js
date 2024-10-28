const totalMatch = (lst1, lst2) => {
  let totalChars = 0;
  let totalChars2 = 0;
  for (let i = 0; i < lst1.length; i++) {
    totalChars += lst1[i].length;
  }
  for (let j = 0; j < lst2.length; j++) {
    totalChars2 += lst2[j].length;
  }
  if (totalChars < totalChars2) {
    return lst1;
  } else {
    return lst2;
  }
};

const totalMatch = (lst1, lst2) => {
  if (lst1.length === lst2.length) {
    return lst1;
  } else if (lst1.length < lst2.length) {
    return lst1;
  } else {
    return lst2;
  }
};
