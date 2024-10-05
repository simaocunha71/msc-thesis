  return l.filter((x, i) => i % 2 == 0).sort().concat(l.filter((x, i) => i % 2 != 0));
}  // Or
const sortEven = (l) => {
  return l.map((x, i) => i % 2 == 0 ? l.slice(i*2, i*2+1).sort()[0] : x);
}  // Or
const sortEven = (l) => {
  return l.slice(0, 1).concat(l.slice(1).slice(0).sort().filter((x, i) => i % 2 == 0));
}  // Or
const sortEven = (l) => {
  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(...l.slice(i*2, i*2+1).sort());
    } else {
      result.push(l[i]);
    }
  }
  return result;
}  // Or
const sortEven = (l) => {
  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(l.slice(i*2, i*2+1).sort()[0]);
    } else {
      result.push(l[i]);
    }
  }
  return result;
}  // Or
const sortEven = (l) => {
  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(...l.slice(i*2, i*2+1).sort());
    } else {
      result.push(l[i]);
    }
  }
  return result;
}  // Or
const sortEven = (l) => {
  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(...l.slice(i*2, i*2+1).sort());
    } else {
      result.push(l[i]);
    }
  }
  return result;
}  // Or
const sortEven = (l) => {
  let result = [];
  for (let i = 0; i < l.length; i++) {
