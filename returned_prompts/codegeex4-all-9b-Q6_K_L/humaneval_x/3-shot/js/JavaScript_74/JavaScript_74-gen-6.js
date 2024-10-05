  const charCount = (arr) => {
    let count = 0;
    for (const str of arr) {
      count += str.length;
    }
    return count;
  }

  const count1 = charCount(lst1);
  const count2 = charCount(lst2);

  if (count1 < count2) {
    return lst1;
  } else if (count1 > count2) {
    return lst2;
  } else {
    return lst1;
  }
}