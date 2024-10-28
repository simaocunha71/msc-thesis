  return x.filter(n => !(n.toString().match(/(0|2|4|6|8)/g))).sort((a, b) => a - b);
}



