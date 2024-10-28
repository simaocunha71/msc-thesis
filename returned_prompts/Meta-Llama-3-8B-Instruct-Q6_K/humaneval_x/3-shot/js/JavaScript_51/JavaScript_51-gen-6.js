  return text.replace(/[aeiou]/gi, '');
}
// The '/[aeiou]/gi' is a regular expression that matches any vowel (both lowercase and uppercase)
// The 'g' flag makes the replacement global, so that all vowels are replaced, not just the first one.
// The 'i' flag makes the replacement case-insensitive, so that both lowercase and uppercase vowels are matched.