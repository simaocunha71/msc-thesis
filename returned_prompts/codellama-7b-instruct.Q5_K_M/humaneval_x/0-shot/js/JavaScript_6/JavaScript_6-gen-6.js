  return paren_string.replace(/[^\(\)]/g, '').match(/[()]/g).map(char => char.length).filter(char => char % 2)
}
