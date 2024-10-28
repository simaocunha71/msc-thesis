  const nums = Array.from({length: n}, (v, i) => i + 1).filter(x => x.toString().length === n);
  const result = nums.filter(x => x.toString().startsWith("1") || x.toString().endsWith("1"));

  return result.length;
}
