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
    let i, j;
    let counter = 0;

    for(i=0; S[i] != "."; i++) {
        for(j=i+1; S[j] != "." && S[j] != "?"; j++){
            if(S[j].charAt(0) === "I") counter += 1;
        }
    }

    return counter;
}

const main = () => {
    console.log("Hello world", isBored("Hello world"), isBored("The sky is blue. The sun is shining. I love this weather"));
};
main();