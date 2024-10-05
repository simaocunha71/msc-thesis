  var words = s.split(' ');
  var ordered = words.map(word => word.split('').sort().join(''));
  return ordered.join(' ');
}