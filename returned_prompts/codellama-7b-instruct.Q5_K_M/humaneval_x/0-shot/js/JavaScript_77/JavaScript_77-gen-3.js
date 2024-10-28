const iscube = (a) => {
  for (let i = 0; i <= a; i++) {
    if (Math.pow(i, 3) === a) {
      return true;
    }
  }
  return false;
}


