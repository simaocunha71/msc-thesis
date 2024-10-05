  let split = txt.trim().split(/\s+/);
  if (split.length > 0) {
    return split;
  } else {
    let comma_split = txt.trim().split(',');
    if (comma_split.length > 0) {
      return comma_split;
    } else {
      let lower_case_letters = 0;
      for (let i = 0; i < txt.length; i++) {
        if (txt.charCodeAt(i) >= 97 && txt.charCodeAt(i) <= 122) {
          lower_case_letters += 1;
        }
      }
      return lower_case_letters;
    }
  }
}



