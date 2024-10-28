const nextSmallest = (lst) => {
    if (lst.length < 2) return null
    const sorted = lst.sort((a, b) => a - b)
    return sorted[1]
}

