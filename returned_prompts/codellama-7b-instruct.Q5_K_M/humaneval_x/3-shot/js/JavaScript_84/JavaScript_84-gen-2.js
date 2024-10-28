  let result = 0;
  let binary = N.toString(2);
  for (const c of binary) {
    result += parseInt(c);
  }
  return result.toString(2);
}



