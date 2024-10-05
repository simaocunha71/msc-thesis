  return x.filter(n => !/[2,4,6,8]/.test(n.toString())).sort((a, b) => a - b);
}