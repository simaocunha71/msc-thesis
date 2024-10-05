  return Array.from(s).filter((c, i) => i % 2 === 0 && c === c.toUpperCase() && 'AEIOU'.includes(c)).length;
}



