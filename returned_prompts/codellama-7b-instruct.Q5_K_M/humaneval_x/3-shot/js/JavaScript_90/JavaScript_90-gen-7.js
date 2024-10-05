  if (lst.length < 2) {
    return null;
  }

  const sorted = lst.sort((a, b) => a - b);

  if (sorted[1] != lst[0]) {
    return null;
  }

  return sorted[2];
}



