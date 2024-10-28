const isBored = (S) => {
  return S.split('.').filter(str => str.startsWith('I')).length +
    S.split('?').filter(str => str.startsWith('I')).length +
    S.split('!').filter(str => str.startsWith('I')).length
}
