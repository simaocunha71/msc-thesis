  return s.replace(/[a-z]/gi, (c) => {
    return (c == c.toLowerCase()) ? c.toUpperCase() : c.toLowerCase();
  });
}



