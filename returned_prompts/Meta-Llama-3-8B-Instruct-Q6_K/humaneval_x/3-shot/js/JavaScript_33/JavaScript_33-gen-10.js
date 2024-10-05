  return l.map((value, index) => {
    return index % 3 === 0 ? l.slice(0, index).concat(...l.slice(index + 1).sort((a, b) => a - b)).slice(index) : value;
  });
}