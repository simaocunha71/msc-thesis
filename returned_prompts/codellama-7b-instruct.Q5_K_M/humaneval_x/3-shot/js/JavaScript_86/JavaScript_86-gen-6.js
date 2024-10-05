  let arr = s.split(' ');
  let result = '';
  for (let i = 0; i < arr.length; i++) {
    let new_word = '';
    let temp = arr[i].split('');
    temp.sort((a, b) => a.charCodeAt() - b.charCodeAt());
    for (let j = 0; j < temp.length; j++) {
      new_word += temp[j];
    }
    result += new_word + ' ';
  }
  return result.trim();
}



