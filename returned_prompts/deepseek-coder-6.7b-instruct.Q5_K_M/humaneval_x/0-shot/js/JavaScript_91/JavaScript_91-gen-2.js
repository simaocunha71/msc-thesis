  let sentences = S.split(/[.?!]/);
  let count = 0;

  for(let i = 0; i < sentences.length; i++) {
    if(sentences[i].trim().startsWith("I")) count++;
  }

  return count;
}

console.log(isBored("Hello world")); // 0
console.log(isBored("The sky is blue. The sun is shining. I love this weather")); // 1
console.log(isBored("I am bored. What's going on?")); // 1
console.log(isBored("I am bored?!")); // 1
console.log(isBored("I like to play soccer. I love to code. What do you like doing?")); // 2

// This code works by splitting the string into an array of sentences 
// using the split function with a regex that matches '.' or '?' or '!' as 
// delimiters. It then loops over each sentence and checks if it starts with 
// the word "I" using the startsWith function. If it does, it increments the 
// count. Finally, it returns the count.

// Note: The split function will also include empty strings if there are 
// multiple delimiters in a row. These empty strings will not be counted 
// as sentences and will not trigger the if condition.

// Also note that the trim function is used to remove leading or trailing 
// whitespace from each sentence before checking if it starts with "I". This 
// is to handle cases where there are spaces before or after the sentence 
// delimiter.

// Finally, the startsWith function is case sensitive. If you want to ignore 
// case, you can convert both the sentence and the target string to lower 
// case before comparing them.

// Also, this code assumes that there are no multiple sentences in one sentence. 
// If there are multiple sentences in one sentence, this code will not work correctly.
// For example, isBored("I am bored. What's going on?") will return 1, but it 
// should return 2. This is because it's treating "What's going on?" as a separate 