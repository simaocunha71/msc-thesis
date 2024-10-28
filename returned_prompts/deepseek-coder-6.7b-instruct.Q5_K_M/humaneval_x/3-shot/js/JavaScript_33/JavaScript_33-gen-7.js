  let sortedThird = l.filter((_, index) => index % 3 === 0).sort((a, b) => a - b);

  return l.map((value, index) => (index % 3 === 0) ? sortedThird.shift() : value);
}



