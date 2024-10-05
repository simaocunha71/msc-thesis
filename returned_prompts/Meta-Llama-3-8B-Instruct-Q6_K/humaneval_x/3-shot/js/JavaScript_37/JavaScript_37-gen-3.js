  return l.slice(0, 1).concat(l.slice(1).slice(0, -1).sort().slice(0, (l.length - 1) / 2).concat(l.slice(-1)));
}