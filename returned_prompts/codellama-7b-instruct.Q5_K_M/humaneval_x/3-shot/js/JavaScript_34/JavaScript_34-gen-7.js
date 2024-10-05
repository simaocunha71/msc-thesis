  return l.sort().filter(function(item, pos, ary) {
    return !pos || item != ary[pos - 1];
  });
}



