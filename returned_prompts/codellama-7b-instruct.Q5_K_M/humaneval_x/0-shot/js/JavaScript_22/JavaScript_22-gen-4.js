const filterIntegers = (values) => {
    return values.filter(x => typeof x == 'number')
}

B:
const filterIntegers = (values) => {
    return values.filter(x => x % 1 === 0)
}

C:
const filterIntegers = (values) => {
    return values.filter(x => typeof x == 'number' && x % 1 === 0)
}

D:
const filterIntegers = (values) => {
    return values.filter(x => typeof x == 'number' && x % 1 === 0)
}