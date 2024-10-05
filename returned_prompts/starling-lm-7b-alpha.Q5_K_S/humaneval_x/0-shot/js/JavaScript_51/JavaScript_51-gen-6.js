    let result = '';

    for (let i = 0; i < text.length; i++) {
      if (text[i] !== 'a' && text[i] !== 'e' && text[i] !== 'i' && text[i] !== 'o' && text[i] !== 'u' && text[i] !== 'A' && text[i] !== 'E' && text[i] !== 'I' && text[i] !== 'O' && text[i] !== 'U') {
        result += text[i];
      }
    }
    return result;
  };



  // Here's a simpler solution:

  const removeVowels = (text) => {
    return text.replace(/[aeiouAEIOU]/g, '');
  };



  // And even shorter with a one-liner:

  const removeVowels = (text) => text.replace(/[aeiouAEIOU]/g, '');



  // Here's another simple solution using the `filter()` method:

  const removeVowels = (text) => {
    return text.split('').filter((char) => {
      return !'aeiouAEIOU'.includes(char);
    }).join('');
  };



  // And here's a solution using the `split()`, `filter()`, and `join()` methods with an arrow function:

  const removeVowels = (text) =>
    text
      .split('')
      .filter(
        (char) => !'aeiouAEIOU'.includes(char)
      )
      .join('');

  // And here's a solution using the `split()`, `map()`, and `join()` methods with an arrow function:

  const removeVowels = (text) =>
    text
      .split('')
      .map(
        (char) => {
          if (!'aeiouAEIOU'.includes(char)) {
            return char;
          }
        }
      )
      .join('');



  // Here's a solution using the `