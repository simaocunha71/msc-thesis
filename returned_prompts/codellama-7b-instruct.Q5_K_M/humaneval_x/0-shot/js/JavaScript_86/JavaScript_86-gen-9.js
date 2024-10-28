const antiShuffle = (s) => {
  return s.split(' ').map(s => s.split('').sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('')).join(' ');
}


