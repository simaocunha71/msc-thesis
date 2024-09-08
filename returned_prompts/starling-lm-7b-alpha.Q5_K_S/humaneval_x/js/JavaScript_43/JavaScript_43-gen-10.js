  let result = false;
  for (let i = 0; i < l.length; i++) {
    for (let j = 0; j < i; j++) {
      if (l[i] + l[j] === 0) {
        result = true;
        break;
      }
    }
  }
  return result;
}



