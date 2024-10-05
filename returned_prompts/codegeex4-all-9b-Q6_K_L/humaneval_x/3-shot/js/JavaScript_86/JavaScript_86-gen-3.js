  return s.split(' ').map(word => word.split('').sort().join('')).join(' ');
}