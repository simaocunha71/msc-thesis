  var count1 = lst1.reduce((sum, str) => sum + str.length, 0);
  var count2 = lst2.reduce((sum, str) => sum + str.length, 0);
  if (count1 <= count2) {
    return lst1;
  } else {
    return lst2;
  }
}



