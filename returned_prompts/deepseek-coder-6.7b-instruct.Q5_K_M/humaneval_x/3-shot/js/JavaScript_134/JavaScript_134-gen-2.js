  let lastChar = txt[txt.length - 1];
  let secondLastChar = txt[txt.length - 2];

  return (lastChar >= 'a' && lastChar <= 'z') || (lastChar >= 'A' && lastChar <= 'Z')
      && (secondLastChar == ' ' || secondLastChar == undefined);
}



