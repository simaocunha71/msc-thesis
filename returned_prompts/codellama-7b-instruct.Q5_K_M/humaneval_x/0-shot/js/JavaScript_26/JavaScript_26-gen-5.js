const removeDuplicates = (numbers) => {
    return numbers.filter((number, index) => {
        return numbers.indexOf(number) === index
    })
}

