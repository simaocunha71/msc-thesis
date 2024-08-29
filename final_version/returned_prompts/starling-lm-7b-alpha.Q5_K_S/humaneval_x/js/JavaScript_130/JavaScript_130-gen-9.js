  let result = [3];
  while (result.length <= n) {
    if (result.length % 2 === 1) {
      result.push(result[result.length - 1] + result[result.length - 2] + result[result.length - 3]);
    } else {
      result.push(result[result.length - 1] + result[result.length - 2] + result[result.length - 3] + result[result.length - 4]);
    }
  }
  return result;
}



