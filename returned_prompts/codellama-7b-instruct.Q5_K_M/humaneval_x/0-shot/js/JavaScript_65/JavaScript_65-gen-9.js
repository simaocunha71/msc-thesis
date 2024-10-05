const circularShift = (x, shift) => {
  const s = `${x}`.split('');
  s.shift();
  s.push(s.shift());
  return s.join('');
};

