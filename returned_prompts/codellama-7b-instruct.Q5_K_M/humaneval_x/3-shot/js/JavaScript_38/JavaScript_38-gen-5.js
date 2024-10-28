  var groups = [];
  for (let i = 0; i < s.length; i += 3) {
    groups.push(s.slice(i, Math.min(i + 3, s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups.push(group[0] + group.slice(1));
  }
  return groups.join('');
}



