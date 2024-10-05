  let result = lst.filter((word) => word.length % 2 == 0);
  return result.sort((a, b) => {
    if (a.length == b.length) return a.localeCompare(b);
    return a.length - b.length;
  });
}