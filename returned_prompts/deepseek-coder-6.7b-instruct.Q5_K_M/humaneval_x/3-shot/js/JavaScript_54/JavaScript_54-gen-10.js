  const countChars = （s）=> （
    s.split（''）.reduce（（acc, char）=> （
      acc[char] ? acc[char]++ : acc[char] = 1, acc
    ）, {}）
  ）

  const count0 = countChars（s0）
  const count1 = countChars（s1）

  for （let char in count0）{
    if （count0[char] ！== count1[char]）{
      return false
    }
  }

  for （let char in count1）{
    if （count0[char] ！== count1[char]）{
      return false
    }
  }

  return true
}



