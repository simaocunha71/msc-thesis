  let result = text.replace(/\s+/g, (match, index) => {
    return index > 0 && index < text.length - 1 ? '-' : '_';
  });

  return result;
}



