const isBored = (S) => {
  let boredoms = 0
  for (let i = 0; i < S.length; i++) {
    if (S[i] === 'I') {
      boredoms++
    }
  }
  return boredoms
}

