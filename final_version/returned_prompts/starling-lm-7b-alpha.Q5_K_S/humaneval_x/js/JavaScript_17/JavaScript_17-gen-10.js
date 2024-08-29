  const notes = music_string.split(" ");
  const result = [];

  for (const note of notes) {
    if (note === "o") {
      result.push(4);
    } else if (note === "o|") {
      result.push(2);
    } else if (note === ".|") {
      result.push(1);
    }
  }

  return result;
}



