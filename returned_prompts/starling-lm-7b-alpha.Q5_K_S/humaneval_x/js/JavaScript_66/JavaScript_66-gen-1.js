  return s.match(/[A-Z]/g).reduce((sum, char) => sum + char.charCodeAt(0), 0);
}



