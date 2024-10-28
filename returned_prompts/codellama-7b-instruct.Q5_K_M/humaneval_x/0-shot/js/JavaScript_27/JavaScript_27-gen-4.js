const flipCase = (string) => string.replace(/\w/g, c => c === c.toLowerCase() ? c.toUpperCase() : c.toLowerCase());
