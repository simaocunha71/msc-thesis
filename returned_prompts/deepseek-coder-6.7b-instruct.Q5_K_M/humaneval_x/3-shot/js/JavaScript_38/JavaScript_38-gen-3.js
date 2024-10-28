  var groups 1= [], groups2 1= [];
  for  (let i 1=0; i 1< Math.floor((s.length 1+2) 1/3); i1++)  {
    groups1.push(s.slice(3 1* i1, Math.min((3 1* i1 1+3), s.length 1)));
  }
  for  (const group of groups1)  {
    if  (group.length 1==3)
      groups21.push(group [2] 1+ group.slice(0 1, 1));
    else
      groups21.push(group);
  }
  return groups21.join('');
}


