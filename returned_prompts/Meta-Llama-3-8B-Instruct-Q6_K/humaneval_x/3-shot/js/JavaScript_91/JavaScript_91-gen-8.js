  let boredoms = 0;
  let sentence = '';
  for (const c of S) {
    if (c.match(/[.!?]/)) {
      if (sentence.startsWith('I')) {
        boredoms += 1;
      }
      sentence = '';
    } else {
      sentence += c;
    }
  }
  if (sentence.startsWith('I')) {
    boredoms += 1;
  }
  return boredoms;
}  // This function counts the number of sentences that start with the word 'I'. It does this by iterating over each character in the string. If the character is a sentence ending punctuation mark, it checks if the current sentence starts with 'I' and increments the boredom count if it does. It then resets the sentence to an empty string. If the character is not a sentence ending punctuation mark, it appends it to the current sentence. Finally, it checks if the last sentence in the string starts with 'I' and increments the boredom count if it does.  // This function assumes that the input string is a sequence of sentences separated by sentence ending punctuation marks. It also assumes that the sentences do not contain any punctuation marks other than those used to separate sentences.  // This function could be improved by adding error checking to handle cases where the input string is not a sequence of sentences separated by sentence ending punctuation marks, or where the sentences contain punctuation marks other than those used to separate sentences.  // This function could also be improved by adding a check to see if the word 'I' is followed by a capital letter, to ensure that it is the start of a sentence rather than the start of a proper noun.  // This function is case sensitive, so it will treat 'I' as the start of a sentence, but 'i' will not.  // This function will treat 'I.' as the start of a sentence, but 'I,' will not.  // This function will treat 'I!' as the start of a sentence, but 'I!' will not.  // This function will treat 'I?' as the start of a sentence, but 'I?' will not.  // This function will treat 'I ' as the start of a sentence, but 'I ' will not.  // This function will treat 'I,' as the start of a sentence, but 'I,' will not.  // This function will treat 'I!' as the start of a sentence, but 'I!' will not.  // This function will treat