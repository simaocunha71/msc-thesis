  let negs = lst.filter(i => i < 0).sort((a, b) => b - a);
  let poss = lst.filter(i => i > 0).sort((a, b) => a - b);

  return [negs.length > 0 ? negs[0] : null, poss.length > 0 ? poss[0] : null];
}