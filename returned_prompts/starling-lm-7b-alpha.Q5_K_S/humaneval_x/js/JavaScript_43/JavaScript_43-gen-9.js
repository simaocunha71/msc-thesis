  let seen = {};
  for (const i of l) {
    if (seen[i + 0] !== undefined) {
      return true;
    }
    seen[i] = true;
  }
  return false;
}



