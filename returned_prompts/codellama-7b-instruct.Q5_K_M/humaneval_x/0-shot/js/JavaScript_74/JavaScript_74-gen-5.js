const totalMatch = (lst1, lst2) => {
  var count1 = 0;
  var count2 = 0;
  for (let i = 0; i < lst1.length; i++) {
    count1 += lst1[i].length;
  }
  for (let j = 0; j < lst2.length; j++) {
    count2 += lst2[j].length;
  }
  if (count1 > count2) {
    return lst2;
  } else {
    return lst1;
  }
};
