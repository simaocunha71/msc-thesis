  let result = [...l];
  let index = 0;
  while (index < result.length) {
    if (result[index] % 3 === 0) {
      result[index] = l[index].toString().split('').sort().join('');
    }
    index += 1;
  }
  return result;
}



