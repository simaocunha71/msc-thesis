  let result = text.split(" ");
  result = result.map(word => {
    if (word.length == 0) {
      return "-";
    } else {
      return word.replace(/\s{2,}/g, "-").replace(/\s/g, "_");
    }
  });

  return result.join(" ");
}



