  let arr = numbers.split(' ');
  arr.sort((a, b) => {
    if (a == "zero") return -1;
    if (b == "zero") return 1;
    return a.length - b.length;
  });
  return arr.join(' ');
}



