  return x.filter(n => !(n.toString().includes('2') || n.toString().includes('4') || n.toString().includes('6') || n.toString().includes('8') || n.toString().includes('0'))).sort((a, b) => a - b);
}



