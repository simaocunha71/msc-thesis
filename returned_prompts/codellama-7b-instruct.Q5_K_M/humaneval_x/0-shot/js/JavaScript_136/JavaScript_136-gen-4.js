const largestSmallestIntegers = (lst) => {
    const negative = lst.filter(x => x < 0)
    const positive = lst.filter(x => x >= 0)
    const largestNegative = negative.reduce((a, b) => a > b ? a : b)
    const smallestPositive = positive.reduce((a, b) => a < b ? a : b)
    return [largestNegative, smallestPositive]
  }
