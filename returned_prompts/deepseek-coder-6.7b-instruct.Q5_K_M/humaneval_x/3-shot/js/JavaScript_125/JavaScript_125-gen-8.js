  if (txt.includes(' ')) {
    return txt.split(' ');
  } else if (txt.includes(',')) {
    return txt.split(',');
  } else {
    let count = 0;
    for (let i = 0; i < txt.length; i++) {
      if (txt[i] === txt[i].toLowerCase() && txt.charCodeAt(i) % 2 === 1) {
        count++;
      }
    }
    return count;
  }
}



