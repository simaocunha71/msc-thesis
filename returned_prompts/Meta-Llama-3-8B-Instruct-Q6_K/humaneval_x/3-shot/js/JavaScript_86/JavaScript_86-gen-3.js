  return s.split(' ').map(word => [...word].sort((a, b) => a.charCodeAt(0) - b.charCodeAt(0)).join('')).join(' ');
}