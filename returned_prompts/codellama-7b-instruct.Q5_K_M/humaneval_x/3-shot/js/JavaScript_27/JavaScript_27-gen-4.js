  return string.toLowerCase().replace(/./g, function(c) {
    return String.fromCharCode(c.charCodeAt(0) ^ 32);
  });
}



