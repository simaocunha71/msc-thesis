  let result = [];
  let regex = /\s|,/;

  while (txt.length > 0) {
    let match = txt.match(regex);
    if (match && match.length == 1) {
      result.push(match[0]);
      txt = txt.replace(match[0], '');
    } else {
      result.push(txt.slice(0, txt.search(/[, ]/)));
      txt = txt.replace(txt.slice(0, txt.search(/[, ]/)), '');
    }
  }

  return result;
}



