const sortEven = (l) => {
  const sorted = l.slice();
  for(let i = 0; i < sorted.length; i += 2) {
    sorted[i] = sorted[i].sort();
  }
  return sorted;
}

B:
const sortEven = (l) => {
  const sorted = [];
  for(let i = 0; i < l.length; i += 2) {
    sorted.push(l[i]);
  }
  return sorted;
}

C:
const sortEven = (l) => {
  const sorted = l.slice();
  for(let i = 0; i < sorted.length; i += 2) {
    sorted[i] = sorted[i].sort();
  }
  return sorted;
}

D:
const sortEven = (l) => {
  const sorted = l.slice();
  for(let i = 0; i < sorted.length; i += 2) {
    sorted[i] = sorted[i].sort();
  }
  return sorted;
}
