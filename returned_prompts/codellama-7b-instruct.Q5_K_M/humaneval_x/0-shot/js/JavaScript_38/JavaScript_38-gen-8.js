  const groups = [];
  for (let i = 0; i < Math.floor(s.length / 3); i++) {
    groups.push(s.slice(3 * i, Math.min((3 * i + 3), s.length)));
  }
  for (const group of groups) {
    if (group.length == 3)
      groups.push(group.slice(1) + group[0]);
    else
      groups.push(group);
  }
  return groups.join('');
}