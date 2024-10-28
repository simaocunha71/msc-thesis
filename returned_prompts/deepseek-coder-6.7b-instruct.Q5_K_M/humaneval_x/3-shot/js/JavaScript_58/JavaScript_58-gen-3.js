  return [...new Set(l1.filter(value => l2.includes(value)))].sort((a, b) => a - b);
}



