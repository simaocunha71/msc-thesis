  let count = 0;
  nums.filter(num => Math.abs(num) > 10 && /^\d{1}(\d|[1-9])$/.test(Math.abs(num).toString())).length;
  return count;
}