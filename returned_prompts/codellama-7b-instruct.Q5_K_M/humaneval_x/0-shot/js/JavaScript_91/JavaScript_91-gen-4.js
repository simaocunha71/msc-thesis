const isBored = (S) => S.split(/[.?!]/).filter(sentence => sentence.startsWith('I')).length;
