  const unique_elements = new Set(l1.concat(l2));
  const common_elements = unique_elements.filter(el => l1.includes(el) && l2.includes(el));
  return common_elements.sort((a, b) => a - b);
}



