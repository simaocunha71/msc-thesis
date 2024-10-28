
const antiShuffle = (s) => {
  let words = s.split(' ');
  let shuffledSentence = '';
  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    let ascArr = [];
    for (let j = 0; j < word.length; j++) {
      ascArr.push(word.charCodeAt(j));
    }
    ascArr.sort((a, b) => a - b);
    shuffledSentence += String.fromCharCode(...ascArr);
    if (i !== words.length - 1) {
      shuffledSentence += ' ';
    }
  }
  return shuffledSentence;
}

// console.log(antiShuffle('Hello World!!!')) // "Hello !!!Wdlor"
