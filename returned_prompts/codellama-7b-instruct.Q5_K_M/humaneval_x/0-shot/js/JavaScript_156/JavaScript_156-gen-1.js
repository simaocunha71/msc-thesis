  const intToRoman = (number) => {
    const romanNumeral = []
    const romanNumerals = [
      { digit: 1000, roman: 'm' },
      { digit: 900, roman: 'cm' },
      { digit: 500, roman: 'd' },
      { digit: 400, roman: 'cd' },
      { digit: 100, roman: 'c' },
      { digit: 90, roman: 'xc' },
      { digit: 50, roman: 'l' },
      { digit: 40, roman: 'xl' },
      { digit: 10, roman: 'x' },
      { digit: 9, roman: 'ix' },
      { digit: 5, roman: 'v' },
      { digit: 4, roman: 'iv' },
      { digit: 1, roman: 'i' },
    ]
    for (const { digit, roman } of romanNumerals) {
      while (number >= digit) {
        romanNumeral.push(roman)
        number -= digit
      }
    }
    return romanNumeral.join('')
  }

  const numberString = number.toString()
  const romanNumeral = intToRoman(number)

  const miniRoman = numberString
    .split('')
    .map((digit, i) => {
      const roman = intToRoman(digit)
      return roman[0]
    })
    .join('')

  return miniRoman
}

