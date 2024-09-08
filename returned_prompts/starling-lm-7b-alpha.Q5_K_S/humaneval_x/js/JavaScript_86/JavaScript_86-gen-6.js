  return s
    .split(' ')
    .map((w) => {
      return w
        .split('')
        .sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0))
        .join('');
    })
    .join(' ');
};



