/*
  You'll be given a string of words, and your task is to count the number
  of boredoms. A boredom is a sentence that starts with the word "I".
  Sentences are delimited by '.', '?' or '!'.
 
  For example:
  >>> isBored("Hello world")
  0
  >>> isBored("The sky is blue. The sun is shining. I love this weather")
  1
  */
const isBored = (S) => {
  const regexp = /[I?!]?([^]+\.|[A-Za-z\s]+)/g
  return S.split(".").reduce((acc, x) => {
    if (!regexp.test(x)) acc += 1;
    return [...acc];
  }, []);
}
