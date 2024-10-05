  return lst.reduce((acc, el, idx) => {
    if (idx % 3 === 0) {
      return acc + Math.pow(el, 2);
    } else if (idx % 4 === 0) {
      return acc + Math.pow(el, 3);
    } else {
      return acc + el;
    }
  }, 0);
}



