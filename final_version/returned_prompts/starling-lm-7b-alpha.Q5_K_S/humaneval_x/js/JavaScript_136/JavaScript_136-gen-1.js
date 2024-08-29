  const neg = lst.filter(num => num < 0);
  const pos = lst.filter(num => num > 0);

  if (neg.length === 0 && pos.length === 0) {
    return [null, null];
  } else if (neg.length === 0) {
    return [null, Math.min(...pos)];
  } else if (pos.length === 0) {
    return [Math.max(...neg), null];
  }

  return [Math.max(...neg), Math.min(...pos)];
}



