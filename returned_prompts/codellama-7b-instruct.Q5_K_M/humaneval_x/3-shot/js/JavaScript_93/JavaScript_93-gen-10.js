  let result = ''
  const vowels = ['a', 'e', 'i', 'o', 'u']
  const vowel_map = {
    a: 'A',
    e: 'E',
    i: 'I',
    o: 'O',
    u: 'U'
  }

  for (const char of message) {
    if (vowels.includes(char)) {
      result += vowel_map[char]
    } else {
      if (char == ' ') {
        result += char
      } else {
        const char_index = char.charCodeAt() - 97
        const next_index = (char_index + 2) % 26
        result += String.fromCharCode(next_index + 97)
      }
    }
  }

  return result
}
