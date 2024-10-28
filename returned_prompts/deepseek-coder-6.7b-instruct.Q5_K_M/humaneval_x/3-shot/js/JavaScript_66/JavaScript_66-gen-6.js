  return s.split('').reduce((total, char) => {
    return char === char.toUpperCase() && char !== char.toLowerCase() ? total + char.charCodeAt(0) : total;
  }, 0);
}



