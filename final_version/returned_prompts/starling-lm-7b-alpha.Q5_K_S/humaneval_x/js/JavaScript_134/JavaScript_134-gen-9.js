  if (txt === "") {
    return false;
  } else if (txt.length === 1 && txt.charCodeAt(0) >= 65 && txt.charCodeAt(0) <= 90) {
    return true;
  } else if (txt.charCodeAt(txt.length - 1) >= 65 && txt.charCodeAt(txt.length - 1) <= 90 && txt[txt.length - 2] === " ") {
    return true;
  } else {
    return false;
  }
}



