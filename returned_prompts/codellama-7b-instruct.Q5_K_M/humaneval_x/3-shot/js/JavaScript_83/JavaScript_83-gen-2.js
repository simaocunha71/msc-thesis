  let count = 0;
  for (let i = 1; i <= n; i++) {
    let num = i.toString();
    if (num[0] == 1 || num[num.length - 1] == 1) {
      count += 1;
    }
  }
  return count;
}



