  return lst.map(str => str.replace(/./g, c => (Number(c) % 2 == 0 ? 'e' : 'o')).replace(/./g, 'n'));
}



