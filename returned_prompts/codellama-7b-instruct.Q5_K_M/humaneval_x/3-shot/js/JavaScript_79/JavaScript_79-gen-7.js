  var binary = 'db'
  while (decimal > 0) {
    if (decimal % 2 == 0) {
      binary = '0' + binary
    } else {
      binary = '1' + binary
    }
    decimal = Math.floor(decimal / 2)
  }
  return binary + 'db'
}



