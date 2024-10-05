  return text.replace(/[aeiouAEIOU]/g, '');
}
// The regular expression [aeiouAEIOU] matches any lowercase or uppercase vowel, and the g flag at the end makes the replacement global, so that all occurrences are replaced, not just the first one.