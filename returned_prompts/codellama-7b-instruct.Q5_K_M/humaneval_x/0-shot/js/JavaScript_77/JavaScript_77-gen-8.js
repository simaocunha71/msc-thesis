const iscube = (a) => {
  for (let i = 1; i < a; i++) {
    if (a === Math.pow(i, 3)) return true;
  }
  return false;
};

