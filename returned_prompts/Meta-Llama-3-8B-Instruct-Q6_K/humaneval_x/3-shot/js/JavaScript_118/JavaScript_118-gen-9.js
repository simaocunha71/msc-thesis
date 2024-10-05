  let result = '';
  for (let i = word.length - 1; i >= 0; i--) {
    if (/^[aeiouAEIOU]$/.test(word[i])) {
      if (/^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]$/.test(word[i - 1]) && /^[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]$/.test(word[i + 1])) {
        result = word[i];
        break;
      }
    }
  }
  return result;
}