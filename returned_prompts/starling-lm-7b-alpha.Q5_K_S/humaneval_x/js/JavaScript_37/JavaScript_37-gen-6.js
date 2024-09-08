  let even_index_sorted = l.slice(1).filter((_, i) => i % 2 === 1).sort((a, b) => a - b);
  return [...l.slice(0, 1), ...even_index_sorted, ...l.slice(l.length % 2)];
}



