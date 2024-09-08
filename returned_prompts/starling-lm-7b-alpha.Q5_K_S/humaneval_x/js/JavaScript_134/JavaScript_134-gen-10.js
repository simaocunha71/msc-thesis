  if (txt == "") return false;
  if (txt[txt.length - 1] == " ") return false;
  if (txt[txt.length - 1] < "a" || txt[txt.length - 1] > "z" && txt[txt.length - 1] < "A" || txt[txt.length - 1] > "Z") return false;
  return true;
}



