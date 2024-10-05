  let lastChar = txt.slice(-1);
  let lastCharIndex = txt.lastIndexOf(lastChar);
  let prevSpaceIndex = txt.slice(0, lastCharIndex).lastIndexOf(' ');
  return (lastChar.match(/[a-zA-Z]/) !== null && prevSpaceIndex === -1);
} 



