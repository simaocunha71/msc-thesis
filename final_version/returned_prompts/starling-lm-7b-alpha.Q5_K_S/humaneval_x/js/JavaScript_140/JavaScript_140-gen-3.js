  let result = text.replace(/\s+/g, (match, p1) => {
    if (match.length == 1) {
      return "_";
    } else {
      return "-";
    }
  });

  return result.replace(/\-+$/g, "_");
}



