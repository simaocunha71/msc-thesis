  return text.replace(/ +/g, function(match) {
    return match.length > 2 ? '-' : '_';
  });
}