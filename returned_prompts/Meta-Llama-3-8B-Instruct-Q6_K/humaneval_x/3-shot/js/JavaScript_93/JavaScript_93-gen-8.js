  let result = '';
  for (const c of message) {
    if (c.toLowerCase() >= 'a' && c.toLowerCase() <= 'z') {
      let charCode = c.charCodeAt(0);
      if (c.toLowerCase() >= 'a' && c.toLowerCase() <= 'z') {
        charCode = (charCode + 2) % 26;
      } else if (c.toLowerCase() >= 'A' && c.toLowerCase() <= 'Z') {
        charCode = (charCode + 2) % 26 + 65;
      }
      result += String.fromCharCode(charCode);
    } else if (c.toLowerCase() >= 'A' && c.toLowerCase() <= 'Z') {
      result += String.fromCharCode(charCode - 65 + 97).toUpperCase();
    } else {
      result += c;
    }
  }
  return result;
}
} 
} 
} }  } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } } }