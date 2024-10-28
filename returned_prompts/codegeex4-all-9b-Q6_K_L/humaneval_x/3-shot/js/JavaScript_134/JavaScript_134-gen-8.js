  var lastChar = txt.charAt(txt.length - 1);
  var lastWord = txt.substring(txt.lastIndexOf(" ") + 1);
  var lastWordLastChar = lastWord.charAt(lastWord.length - 1);
  if (lastChar == " " && lastWordLastChar.match(/[a-z]/i) != null) {
    return true;
  } else {
    return false;
  }
}

