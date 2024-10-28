  let commonSet = new Set([...l1].filter(value => l2.includes(value)));
  return [...commonSet].sort((a, b) => a - b);
}



