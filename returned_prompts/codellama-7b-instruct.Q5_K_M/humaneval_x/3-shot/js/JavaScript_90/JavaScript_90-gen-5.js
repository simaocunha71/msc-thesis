  if (lst.length < 2) return null;
  
  const sorted = lst.sort((a, b) => a - b);
  
  const secondSmallest = sorted[1];
  
  return secondSmallest;
}



