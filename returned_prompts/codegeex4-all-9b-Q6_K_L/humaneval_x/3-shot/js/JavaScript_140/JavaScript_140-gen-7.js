  return text.replace(/\s+/g, (match) => {
    if (match.length > 2) {
      return "-";
    } else {
      return "_";
    }
  });
}



