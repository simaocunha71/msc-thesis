  return a.split('').map((c, i) => (c ^ b[i % b.length])).join('');
}