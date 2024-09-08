  if (txt == "") return false;
  let lastChar = txt[txt.length - 1];
  if (!/[a-zA-Z]/.test(lastChar)) return false;
  let index = txt.lastIndexOf(' ');
  if (index == txt.length - 1) return true;
  return false;
}



