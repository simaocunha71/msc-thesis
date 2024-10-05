  return Math.max(...l);
}
//OR
const maxElement = (l) => {
  let max = l[0];
  for (let i = 1; i < l.length; i++) {
    if (l[i] > max) {
      max = l[i];
    }
  }
  return max;
}  //OR
const maxElement = (l) => l.reduce((a, b) => a > b ? a : b);  //using reduce() method
//OR
const maxElement = (l) => Math.max.apply(null, l);
//OR
const maxElement = (l) => l.sort((a, b) => b - a)[0];
//OR
const maxElement = (l) => [...l].sort((a, b) => b - a)[0];
//OR
const maxElement = (l) => l.reduce((max, current) => current > max ? current : max, l[0]);
//OR
const maxElement = (l) => l.sort((a, b) => b - a).shift();




