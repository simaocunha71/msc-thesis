  const values = [];
  for (const node of arr) {
    if (node % 2 === 0) {
      values.push([node, node]);
    }
  }
  if (values.length === 0) {
    return [];
  }
  values.sort((a, b) => a[0] - b[0]);
  return values[0];
}



