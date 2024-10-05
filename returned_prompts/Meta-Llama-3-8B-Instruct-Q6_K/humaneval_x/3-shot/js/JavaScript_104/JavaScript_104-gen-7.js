  return x.filter(num => !/\d/.test(String(num).replace(/./g, function(c){return /\d/.test(c) ? c : ''}))).sort((a, b) => a - b);
}