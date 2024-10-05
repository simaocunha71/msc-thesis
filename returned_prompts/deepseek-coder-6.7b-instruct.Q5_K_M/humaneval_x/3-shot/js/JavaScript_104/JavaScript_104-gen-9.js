  return x.filter(n => !(n.toString().match(/[02468]/))).sort((a,b) => a - b);
}



