  return s.split(' ').map(word => [...word].sort((a, b) => a.charCodeAt() - b.charCodeAt()).join('')).join(' ');
}