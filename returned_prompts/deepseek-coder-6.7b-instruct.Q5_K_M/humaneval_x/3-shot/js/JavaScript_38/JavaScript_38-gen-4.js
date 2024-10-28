  const decodeCyclic = (s) => {
  var groups = [], raw_s = s;
  for (let i = 0; i < Math.floor((raw_s.length + 2) / 3); i++) {
    groups.push(raw_s.slice(3 * i, Math.min((3 * i + 3), raw_s.length)));
  }
  var groups2 = [];
  for (const group of groups) {
    if (group.length == 3)
      groups2.push(group[2] + group.slice(0, 2));
    else
      groups2.push(group);
  }
  return groups2.join('');
}



