  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    let num = Math.ceil(lst[i]);
    sum += num ** 2;
  }
  return sum;
}



