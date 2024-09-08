  if (lst1.length > lst2.length) {
    return lst2;
  } else if (lst1.length < lst2.length) {
    return lst1;
  } else {
    let result = [];
    let sum = 0;
    for (let i = 0; i < lst1.length; i++) {
      sum += lst1[i].length;
    }
    for (let i = 0; i < lst2.length; i++) {
      result.push(lst2[i]);
    }
    if (sum < lst2.length) {
      return result;
    } else {
      return lst1;
    }
  }
}



