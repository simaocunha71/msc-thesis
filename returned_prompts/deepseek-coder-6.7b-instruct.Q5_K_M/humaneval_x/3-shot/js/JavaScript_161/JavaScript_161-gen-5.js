  let reversed 
    
  if  (s.match(/[a-z]/i)) 
    reversed = s.split('').map(c => c === c.toUpperCase() ? c.toLowerCase() : c.toUpperCase()).join('');
  else 
    reversed = s.split('').reverse().join('');

  return reversed;
}



