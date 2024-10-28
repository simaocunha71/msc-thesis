const fixSpaces = text => 
  text
    .replace(/\s+/g, (m) => m.length > 1 ? '-' : '_')
    .replace(/^_|_$/g, '')
