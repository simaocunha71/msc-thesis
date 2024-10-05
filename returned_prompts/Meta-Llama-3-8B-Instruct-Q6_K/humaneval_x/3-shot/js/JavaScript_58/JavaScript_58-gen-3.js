  let set1 = new Set(l1);
  let set2 = new Set(l2);
  let intersection = new Set([...set1].filter(x => set2.has(x)));
  return Array.from(intersection).sort((a, b) => a - b);
}
// OR
const common = (l1, l2) => {
  return [...new Set(l1)].filter(x => l2.includes(x)).sort((a, b) => a - b);
}
// OR
const common = (l1, l2) => {
  return l1.filter(x => l2.includes(x)).sort((a, b) => a - b);
}
// OR
const common = (l1, l2) => {
  return l1.filter(x => l2.includes(x)).sort((a, b) => a - b).filter((value, index, self) => self.indexOf(value) === index);
}
// OR
const common = (l1, l2) => {
  let result = [];
  for (let i = 0; i < l1.length; i++) {
    for (let j = 0; j < l2.length; j++) {
      if (l1[i] === l2[j] && !result.includes(l1[i])) {
        result.push(l1[i]);
      }
    }
  }
  return result.sort((a, b) => a - b);
}