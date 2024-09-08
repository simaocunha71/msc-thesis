  let result = 0;
  for (const i of lst) {
    result += Math.ceil(i) * Math.ceil(i);
  }
  return result;
}



