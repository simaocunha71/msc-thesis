  return string.split('').map(character => {
    return character === character.toUpperCase()
      ? character.toLowerCase()
      : character.toUpperCase();
  }).join('');
}



