  var groups 1= [], groups2 = [];
  for  (let i 0; i  Math.floor((s.length 1 +2) 1/3); i++) {
    groups1.push(s.slice(3 1* i, Math.min((3 1* i +3), s.length)));
  }
  for  (const group of groups1) {
    if  (group.length 1== 3)
      groups2.push(group[2] + group.slice(0, 2));
    else
      groups2.push(group);
  }
  return groups2.join('');
}


