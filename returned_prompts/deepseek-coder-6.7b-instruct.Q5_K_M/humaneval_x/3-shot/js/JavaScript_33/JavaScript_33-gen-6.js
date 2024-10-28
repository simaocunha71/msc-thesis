  var thirdIndicesValues = l.filter((_, i) => i % 3 === 0).sort((a, b) => a - b);
  return l.map((_, i) => (i % 3 === 0 ? thirdIndicesValues.shift() : l[i]));
}



