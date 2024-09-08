  return s.match(/[A-Z]/g)?.reduce((a, b) => a + b.charCodeAt(0), 0);
}



