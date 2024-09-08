  let countOdd = lst1.filter(num => num % 2 !== 0).length;
  let countEven = lst2.filter(num => num % 2 === 0).length;

  if (countEven >= countOdd) {
    return "YES";
  } else {
    return "NO";
  }
}



