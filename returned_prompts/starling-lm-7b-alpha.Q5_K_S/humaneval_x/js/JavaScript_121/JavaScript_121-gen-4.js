  let result = 0;
  let count = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 2 === 0 && lst[i] % 2 === 1) {
      result += lst[i];
    }
  }
  return result;
}


