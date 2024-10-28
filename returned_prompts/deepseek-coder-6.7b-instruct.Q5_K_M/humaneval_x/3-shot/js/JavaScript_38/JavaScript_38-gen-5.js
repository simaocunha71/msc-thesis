  var groups  , groups2  = [] , s.length  % 3 == 0 ? 
  (groups = Array.from({length: Math.floor(s.length  / 3)}, (_, i) => s.slice(3  * i, 3  * i  + 3))) : 
  (groups = Array.from({length: Math.floor(s.length  / 3) + 1}, (_, i) => s.slice(3  * i, Math.min(3  * i  + 3, s.length))), 
  groups[groups.length - 1] = groups[groups.length - 1].padEnd(3, ' ')), 
  (groups2 = Array.from({length: groups.length}, () => ''))
  for  (let i  in groups)
    groups2[i] = groups[i][2] + groups[i].substr(0, 2)
  return groups2.join('')
}



