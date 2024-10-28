  return s.split(/,?\s+/);
}
// or
const wordsString = (s) => {
  return s.split(/[\s,]+/);
}
// or
const wordsString = (s) => {
  return s.replace(/[\s,]+/g, ',').split(',');
}
// or
const wordsString = (s) => {
  return s.trim().split(/[\s,]+/);
}
// etc... there are many ways to do this, depends on how you want to handle extra spaces and commas.
// The above examples are using regular expressions to split the string.
// The first one uses a non-greedy match to split on commas or spaces.
// The second one uses a character class to match either a space or a comma.
// The third one uses a global replace to replace all occurrences of commas or spaces with a single comma.
// The fourth one trims the string before splitting it.
// You can choose the one that best fits your needs.