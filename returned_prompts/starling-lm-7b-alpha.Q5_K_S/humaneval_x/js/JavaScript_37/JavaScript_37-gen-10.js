  let result = [...l];
  for (let i = 0; i < result.length; i++) {
    if (i % 2 === 0) {
      continue;
    }
    const index = Math.floor(i / 2);
    const temp = result[i];
    result[i] = result[index];
    result[index] = temp;
  }
  result.sort((a, b) => a - b);
  return result;
}



