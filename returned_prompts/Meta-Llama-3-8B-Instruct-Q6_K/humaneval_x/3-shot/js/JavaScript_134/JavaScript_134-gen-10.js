  let last_char = txt.slice(-1);
  let is_last_char_alphabetic = last_char.match(/[a-zA-Z]/);
  let is_last_char_part_of_word = txt.match(/[^ ]*$/)[0].slice(-1) == last_char;
  return is_last_char_alphabetic && !is_last_char_part_of_word;
}
// or
const checkIfLastCharIsALetter = (txt) => {
  let last_char = txt.slice(-1);
  return last_char.match(/[a-zA-Z]/) && txt.trim().slice(-1) != last_char;
}