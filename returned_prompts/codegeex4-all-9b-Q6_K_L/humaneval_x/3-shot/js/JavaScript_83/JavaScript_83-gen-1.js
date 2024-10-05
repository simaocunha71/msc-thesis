  let count = 0;
  for (let i = 1; i < Math.pow(10, n); i++) {
    let str = i.toString();
    if (str.startsWith('1') || str.endsWith('1')) {
      count += 1;
    }
  }
  return count;
}



