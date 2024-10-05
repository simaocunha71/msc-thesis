  let evenIndices = l.filter((_, index) => index % 2 === 0).sort((a, b) => a - b);
  return l.map((_, index) => (index % 2 === 0) ? evenIndices.shift() : l[index]);
}



