const cycpatternCheck = (a, b) => {
    const check = (word) => {
        return a.includes(word)
    }
    const rotations = (word) => {
        const len = word.length
        const arr = word.split('')
        const rot = (len - 1) * arr.length
        const rotated = arr.concat(arr).splice(0, rot)
        return rotated.join('')
    }
    let isSub = false
    for (let i = 0; i < b.length; i++) {
        if (check(b[i])) {
            isSub = true
            break
        }
    }
    for (let i = 0; i < b.length; i++) {
        if (check(rotations(b[i]))) {
            isSub = true
            break
        }
    }
    return isSub
}
console.log(cycpatternCheck("abcd","abd"))
console.log(cycpatternCheck("hello","ell"))
console.log(cycpatternCheck("whassup","psus"))
console.log(cycpatternCheck("abab","baa"))
console.log(cycpatternCheck("efef","eeff"))
console.log(cycpatternCheck("himenss","simen"))
