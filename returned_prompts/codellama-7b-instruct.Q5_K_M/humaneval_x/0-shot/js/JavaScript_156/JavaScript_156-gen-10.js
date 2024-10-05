const intToRoman = require('./intToRoman')

const intToMiniRoman = (number) => {
  return intToRoman(number).replace(/M{2,}/g, 'M').replace(/D{2,}/g, 'D').replace(/C{2,}/g, 'C').replace(/X{2,}/g, 'X').replace(/V{2,}/g, 'V').replace(/I{2,}/g, 'I')
}

module.exports = intToMiniRoman
