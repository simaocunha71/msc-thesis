  let result = [];
  let seen = {};

  for (let i = 0; i < l.length; i++) {
    if (seen[l[i]]) {
      continue;
    }
    seen[l[i]] = true;
    result.push(l[i]);
  }

  return result.sort((a, b) => a - b);
}



