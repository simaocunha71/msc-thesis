  return x.filter(n => !(n.toString().match(/[2468]/))).sort((a, b) => a - b);
}



