/*
  function sortArray(arr) {
    return arr.sort((a, b) => {
      const [aOnes, aZeros] = a.toString(2).match(/1/g).length,
        [bOnes, bZeros] = b.toString(2).match(/1/g).length
      return aOnes - bOnes || aZeros - bZeros || a - b
    })
  }
*/
B:
/*
  function sortArray(arr) {
    return arr.sort((a, b) => {
      const aOnes = a.toString(2).match(/1/g).length
      const bOnes = b.toString(2).match(/1/g).length
      if (aOnes === bOnes) return a - b
      else return aOnes - bOnes
    })
  }
*/
C:
/*
  function sortArray(arr) {
    return arr.sort((a, b) => {
      const aOnes = a.toString(2).match(/1/g).length
      const bOnes = b.toString(2).match(/1/g).length
      if (aOnes === bOnes) return a - b
      else return aOnes - bOnes
    })
  }
*/
D:
/*
  function sortArray(arr) {
    return arr.sort((a, b) => {
      const aOnes = a.toString(2).match(/1/g).length
      const bOnes = b.toString(2).match(/1/g).length
      if (aOnes === bOnes) return a - b
      else return aOnes - bOnes
    })
  }
*/
E:
/*
  function sortArray(arr) {
    return arr.sort((a, b) => {
      const aOnes = a.toString(2).match(/1/g).length
      const bOnes = b.toString(2).match(/1/g).length
      if (aOnes === bOnes) return a - b
      else return aOnes - bOnes
    })
  }
