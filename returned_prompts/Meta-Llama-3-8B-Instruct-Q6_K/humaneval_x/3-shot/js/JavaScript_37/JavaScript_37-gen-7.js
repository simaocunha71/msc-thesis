  return l.slice(0, 1).concat(l.slice(1).slice(0, 1).sort().concat(l.slice(1).slice(1)));
}