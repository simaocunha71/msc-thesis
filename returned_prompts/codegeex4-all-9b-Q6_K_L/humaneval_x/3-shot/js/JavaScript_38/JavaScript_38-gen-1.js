  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group.slice(2) + group[0]);
    else
      groups2.push(group);
  }
  return groups2.join('');
}

/*
  takes as input string encoded with encode_cyclic function and returns number of
  characters that were shifted in original string.
  */
const cyclicShifted = (s) => {
  var groups = [], groups2 = [];
  for (let i = 0; i < Math.floor((s.length + 2) / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group.slice(2) + group[0]);
    else
      groups2.push(group);
  }
  return groups2.join('');
}

