const histogram = (test) => {
    if (test === '') return {}
    const letters = test.split(' ')
    const letterCount = {}
    for (const letter of letters) {
        if (letterCount[letter]) {
            letterCount[letter]++
        } else {
            letterCount[letter] = 1
        }
    }
    const maxCount = Math.max(...Object.values(letterCount))
    const mostRepeated = Object.keys(letterCount).filter(key => letterCount[key] === maxCount)
    const result = {}
    for (const key of mostRepeated) {
        result[key] = maxCount
    }
    return result
}