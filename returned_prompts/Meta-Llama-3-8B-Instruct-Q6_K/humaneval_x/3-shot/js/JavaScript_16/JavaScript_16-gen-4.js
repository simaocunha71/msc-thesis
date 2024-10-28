  let charSet = new Set(string.toLowerCase());
  return charSet.size;
}  // or return [...new Set(string.toLowerCase())].length; for older browsers that don't support Set.size



