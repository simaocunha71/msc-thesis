  let result = [];
  for (const n of numbers) {
    if (!result.includes(n)) {
      result.push(n);
    }
  }
  return result;
}



