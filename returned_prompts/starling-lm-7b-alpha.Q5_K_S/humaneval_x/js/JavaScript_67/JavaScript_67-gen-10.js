  let a = s.match(/(\d+)\s*(?:apples)?/);
  let o = s.match(/(\d+)\s*(?:oranges)?/);
  return n - (+a[1]) - (+o[1]);
}



