  return text.replace(/\s+/g, match => {
    if (match.length === 1) {
      return "_";
    } else {
      return "-";
    }
  });
}



