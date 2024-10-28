  const arrProd = arr.reduce((a, b) => a * b, 1)
  const arrSum = arr.reduce((a, b) => a + Math.abs(b), 0)
  const arrSigns = arr.map((x) => (x < 0) ? -1 : 1)
  const arrSignsProd = arrSigns.reduce((a, b) => a * b, 1)
  return arrSum * arrSignsProd / arrProd
}
