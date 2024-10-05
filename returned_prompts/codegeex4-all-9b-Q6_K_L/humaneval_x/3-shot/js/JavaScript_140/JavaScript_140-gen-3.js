  return text.replace(/\s+/g, function(match) {
    return match.length > 2 ? '-' : '_';
  });
}