  return x.filter(num => !/\d/.test(num.toString().replace(/./g, function(a){return a%2===0?'':a}))).sort((a, b) => a - b);
}