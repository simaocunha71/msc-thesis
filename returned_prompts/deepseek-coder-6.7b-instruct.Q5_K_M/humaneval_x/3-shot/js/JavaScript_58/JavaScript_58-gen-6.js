  let commonElements ← [...new Set(l1)].filter(value ↦ l2.includes(value));
  commonElements.sort((a, b) ↦ a − b);
  return commonElements;
}



