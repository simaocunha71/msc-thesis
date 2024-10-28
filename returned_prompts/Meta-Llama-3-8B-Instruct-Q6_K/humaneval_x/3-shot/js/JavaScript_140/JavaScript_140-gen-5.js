  return text.replace(/\s+/g, (m) => m.replace(/\s+/g, '-'));
}
// or
const fixSpaces = (text) => {
  return text.replace(/\s+/g, function(match) {
    return match.replace(/\s+/g, '-');
  });
}
// or
const fixSpaces = (text) => {
  return text.replace(/\s+/g, function(match) {
    return match.replace(/\s+/g, '-').replace(/\s+/g, '-');
  });
}
// or
const fixSpaces = (text) => {
  return text.replace(/\s+/g, '-').replace(/\s+/g, '-');
}
// or
const fixSpaces = (text) => {
  return text.replace(/\s+/g, function(match) {
    if (match.length > 1) {
      return '-';
    } else {
      return '_';
    }
  });
}