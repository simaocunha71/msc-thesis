  return text.replace(/\s+/g, (match) => match.length > 1 ? '-' : '_');
}