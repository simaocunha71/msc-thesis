  if (arr.length === 0) return true;

  let sortedArr = [...arr].sort((a, b) => a - b);
  for (let i = 0; i < arr.length; i++) {
    if (JSON.stringify(arr) === JSON.stringify(sortedArr)) return true;
    arr.unshift(arr.pop());
  }
  return false;
}



