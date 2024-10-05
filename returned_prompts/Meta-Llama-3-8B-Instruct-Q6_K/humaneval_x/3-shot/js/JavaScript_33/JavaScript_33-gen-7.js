  return l.map((v, i) => i % 3 !== 0 ? v : l.slice(0, i).concat(l.slice(i + 1)).sort()[0]);
}
// Alternative solution
const sortThird = (l) => {
  return l.map((v, i) => i % 3 !== 0 ? v : (l.filter((x, j) => j % 3 === i)[0]));
}
// Alternative solution
const sortThird = (l) => {
  return l.map((v, i) => i % 3 !== 0 ? v : Math.min(...l.filter((x, j) => j % 3 === i)));
}
// Alternative solution
const sortThird = (l) => {
  return l.map((v, i) => i % 3 !== 0 ? v : l.slice(i).filter(x => x)[0]);
}