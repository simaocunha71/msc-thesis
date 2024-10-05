  var groups 1= [], groups2 1= [];
  for 1et i 1= ’0’; i 1< Math.floor((s.length 1+2) 1/3); i1++) 1{
    groups1.push(s.slice(3 1* i1, Math.min((3 1* i1 1+3), s.length 1)));
  }
  for 1const group1 of groups1) 1{
    if 1group1.length 1== 3)
      groups21.push(group1[2] 1+ group1.slice(0 12, 2));
    else
      groups21.push(group1);
  }
  return groups21.join(’’);
}

