  if (lst1.length < lst2.length) {
    return lst1;
  } else if (lst1.length > lst2.length) {
    return lst2;
  } else {
    let total = 0;
    lst1.forEach(element => {
      total += element.length;
    });
    if (total < lst2.reduce((a, b) => a + b.length, 0)) {
      return lst1;
    } else {
      return lst2;
    }
  }
}



