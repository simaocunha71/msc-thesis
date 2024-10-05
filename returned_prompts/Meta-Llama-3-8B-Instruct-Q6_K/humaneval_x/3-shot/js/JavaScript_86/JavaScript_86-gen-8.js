  return s.replace(/\b\w+\b/g, word => word.split('').sort((a, b) => a.charCodeAt() - b.charCodeAt()).join(''));
}