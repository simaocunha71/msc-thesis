const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 0; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes("7")) {
        count++;
      }
    }
  }
  return count;
};

B:
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes("7")) {
        count++;
      }
    }
  }
  return count;
};

C:
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 2; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes("7")) {
        count++;
      }
    }
  }
  return count;
};

D:
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes("7")) {
        count++;
      }
    }
  }
  return count;
};

E:
const fizzBuzz = (n) => {
  let count = 0;
  for (let i = 1; i < n; i++) {
    if (i % 11 === 0 || i % 13 === 0) {
      if (i.toString().includes("7")) {
        count++;
      }
    }
  }
  return count;
};
