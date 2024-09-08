  return arr.sort((a, b) => {
    const sa = (a | (1 << 31)).toString(2).split('1').length - 1;
    const sb = (b | (1 << 31)).toString(2).split('1').length - 1;
    return sa != sb ? sa - sb : a - b;
  });
}



