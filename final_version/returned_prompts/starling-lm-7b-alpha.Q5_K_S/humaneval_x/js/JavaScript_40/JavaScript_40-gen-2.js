  let set = new Set(l);
  let len = set.size;
  for (let i = 0; i < len; i++) {
    let curr = set.values().next().value;
    for (let j = 0; j < len; j++) {
      let other = set.values().next().value;
      if (curr + other + curr + other + other === 0) {
        return true;
      }
    }
  }
  return false;
}



