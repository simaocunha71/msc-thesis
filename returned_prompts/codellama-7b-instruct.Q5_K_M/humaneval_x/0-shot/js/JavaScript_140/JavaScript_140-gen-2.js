const fixSpaces = (text) => {
  return text.replace(/\s+/g, (match, i) => i ? '-' : '_');
}


