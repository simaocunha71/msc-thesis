const selectWords = (s, n) => {
  // If the string is empty, return an empty array
  if (!s.length) return [];

  // Split the string into an array of words
  const words = s.split(" ");

  // Filter the array to only include words that have n consonants
  const consonantWords = words.filter(word => {
    const vowels = ["a", "e", "i", "o", "u"];
    const consonants = word.split("").filter(char => !vowels.includes(char));
    return consonants.length === n;
  });

  // Return the array of words
  return consonantWords;
};



