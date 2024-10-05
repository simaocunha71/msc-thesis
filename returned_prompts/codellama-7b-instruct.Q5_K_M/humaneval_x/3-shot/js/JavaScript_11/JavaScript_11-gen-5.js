  return a.split('').map(function(x, i) {
    return +(x ^ b[i]);
  }).join('');
}



