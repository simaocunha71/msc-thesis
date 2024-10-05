  return text.replace(/\s+/g, (match) => {
    return match.length > 1 ? '-' : '_';
  });
}