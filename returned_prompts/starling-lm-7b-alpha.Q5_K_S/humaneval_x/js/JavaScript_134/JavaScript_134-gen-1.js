  return (txt.length > 0 && txt[txt.length - 1].match(/[a-zA-Z]/))
    && !txt.match(/\s$/, '')
    && !txt.match(/\s.*\s$/, '');
}



