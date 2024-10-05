  if  (txt.includes(' '))  {
    return txt.split(' ');
  } else if  (txt.includes(','))  {
    return txt.split(',');
  } else  {
    return  Math.floor(txt.split('').filter((c) => c === c.toLowerCase() && c.charCodeAt(0) % 2 === 1).length / 2);
  }
}



