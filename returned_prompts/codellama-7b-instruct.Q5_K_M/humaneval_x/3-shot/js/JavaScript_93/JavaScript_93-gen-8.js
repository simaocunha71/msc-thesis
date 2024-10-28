  let encoded = '';
  let current_letter;
  let next_letter;
  let next_next_letter;

  for (let i = 0; i < message.length; i++) {
    current_letter = message[i];
    if (current_letter === ' ') {
      encoded += current_letter;
      continue;
    }
    if (current_letter.toUpperCase() === 'E' || current_letter.toUpperCase() === 'I' || current_letter.toUpperCase() === 'O' || current_letter.toUpperCase() === 'U') {
      next_letter = message[i + 1];
      next_next_letter = message[i + 2];
      encoded += next_letter;
      encoded += next_next_letter;
      i += 2;
      continue;
    }
    if (current_letter.toUpperCase() === 'A' || current_letter.toUpperCase() === 'E' || current_letter.toUpperCase() === 'I' || current_letter.toUpperCase() === 'O' || current_letter.toUpperCase() === 'U') {
      next_letter = message[i + 1];
      next_next_letter = message[i + 2];
      encoded += next_letter;
      encoded += next_next_letter;
      i += 2;
      continue;
    }
    if (current_letter.toUpperCase() === 'B' || current_letter.toUpperCase() === 'C' || current_letter.toUpperCase() === 'D' || current_letter.toUpperCase() === 'F' || current_letter.toUpperCase() === 'G') {
      next_letter = message[i + 1];
      next_next_letter = message[i + 2];
      encoded += next_letter;
      encoded += next_next_letter;
      i += 2;
      continue;
    }
    if (current_letter.toUpperCase() === 'H' || current_letter.toUpperCase() === 'J' || current_letter.toUpperCase() === 'K' || current_letter.toUpperCase() === 'L