const totalMatch = (lst1, lst2) => {
    if (lst1.length === 0 || lst2.length === 0) return []
    let charCount = 0
    for (let i = 0; i < lst1.length; i++) {
        for (let j = 0; j < lst2.length; j++) {
            charCount += lst1[i].length
            charCount += lst2[j].length
        }
    }
    if (charCount < lst2.length) {
        return lst1
    } else {
        return lst2
    }
}




