  return s.split(' ').sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
      if (a.charCodeAt(i) > b.charCodeAt(i)) {
        return 1;
      } else if (a.charCodeAt(i) < b.charCodeAt(i)) {
        return -1;
      }
    }
    return 0;
  }).join(' ');
}



