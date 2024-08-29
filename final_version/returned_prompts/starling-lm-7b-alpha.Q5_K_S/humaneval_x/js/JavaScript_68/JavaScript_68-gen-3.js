  let result = [Infinity, Infinity];
  for (let i = 0; i < arr.length; i++) {
    let node = arr[i];
    if (node % 2 === 0 && node < result[0]) {
      result = [node, i];
    }
  }
  return result;
}



