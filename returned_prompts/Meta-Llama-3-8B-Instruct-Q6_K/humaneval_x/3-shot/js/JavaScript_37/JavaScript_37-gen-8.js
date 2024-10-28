  return l.map((x, i) => i % 2 === 0 ? [...l].slice(0, i).concat([...l].slice(i+1)).sort((a, b) => a - b)[0] : x);
} 



