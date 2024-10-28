  return text.replace(/\s+/g, function(match) {
    return match.length > 1 ? '-' : '_';
  });
}
// This solution uses a regular expression to match one or more whitespace characters. The callback function is then called for each match, and it returns a string that replaces the match with either an underscore if the match is a single space, or a hyphen if the match has more than one space. The replace method is then called with the regular expression and the callback function as arguments, and the result is returned.