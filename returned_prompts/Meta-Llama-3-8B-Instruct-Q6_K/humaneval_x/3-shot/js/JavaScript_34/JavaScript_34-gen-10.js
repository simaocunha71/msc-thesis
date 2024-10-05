  return [...new Set(l)].sort((a, b) => a - b);
}
// Another solution:
const unique = (l) => {
  let result = [];
  for (let i = 0; i < l.length; i++) {
    let found = false;
    for (let j = 0; j < result.length; j++) {
      if (l[i] === result[j]) {
        found = true;
        break;
      }
    }
    if (!found) {
      result.push(l[i]);
    }
  }
  return result.sort((a, b) => a - b);
}