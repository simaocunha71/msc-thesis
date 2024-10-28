/*
  let arr = [];
  for (let i = 2; i < n; i++) {
      if (i % 2 === 0) {
          arr.push(i);
      }
  }
  return arr;
  */
const countUpTo = (n) => {
  let arr = [];
  for (let i = 2; i < n; i++) {
      if (i % 2 !== 0) {
          arr.push(i);
      }
  }
  return arr;
}


