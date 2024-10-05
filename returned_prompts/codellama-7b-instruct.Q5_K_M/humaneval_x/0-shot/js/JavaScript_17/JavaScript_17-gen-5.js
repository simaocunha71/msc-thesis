const parseMusic = music_string => [
  'o o| .| o| o| .| .| .| .| o o'.match(/o/g) || [],
  'o o| .| o| o| .| .| .| .| o o'.match(/o\|/g) || [],
  'o o| .| o| o| .| .| .| .| o o'.match(/\.\|/g) || [],
].reduce((acc, curr) => acc.concat(curr.length), []);
