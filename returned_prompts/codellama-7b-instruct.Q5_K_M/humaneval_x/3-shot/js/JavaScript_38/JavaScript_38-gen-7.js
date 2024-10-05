  var groups = [];
  for (let i = 0; i < s.length; i += 3) {
    groups.push(s.slice(i, Math.min(i + 3, s.length)));
  }
  for (let i = 0; i < groups.length; i++) {
    groups[i] = groups[i].slice(1) + groups[i][0];
  }
  return groups.join('');
}



