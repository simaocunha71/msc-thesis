  return [...new Set(l1.filter(x => l2.includes(x)))]
    .sort((a, b) => a - b);
}  // or
const common = (l1, l2) => {
  return l1.filter(x => l2.includes(x)).sort((a, b) => a - b);
}  // or
const common = (l1, l2) => {
  let result = [];
  for (let i of l1) {
    if (l2.includes(i) && !result.includes(i)) {
      result.push(i);
    }
  }
  return result.sort((a, b) => a - b);
}  // or
const common = (l1, l2) => {
  let result = [];
  for (let i of l2) {
    if (l1.includes(i) && !result.includes(i)) {
      result.push(i);
    }
  }
  return result.sort((a, b) => a - b);
}  // or
const common = (l1, l2) => {
  let result = [];
  for (let i of l1) {
    if (l2.includes(i)) {
      if (!result.includes(i)) {
        result.push(i);
      }
    }
  }
  return result.sort((a, b) => a - b);
}  // or
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
}  // or
const common = (l1, l2) => {
  let result = [];
  for (let i = 0; i < l1.length; i++) {
    if (l2.includes(l1[i])) {
      if (!result.includes(l1[i])) {
        result.push(l1[i]);
      }
    }
  }
  return result.sort((a, b) => a - b);
}  // or
const common = (l1, l2) => {
  let result = [];
  for (let i = 0; i < l1