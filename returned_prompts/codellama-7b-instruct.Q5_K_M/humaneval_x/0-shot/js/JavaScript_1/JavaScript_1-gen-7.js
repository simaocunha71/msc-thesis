const separateParenGroups = (paren_string) => {
    const paren_list = []
    let paren_group = ''

    for (let i = 0; i < paren_string.length; i++) {
        if (paren_string[i] === '(') {
            paren_group += paren_string[i]
        } else if (paren_string[i] === ')') {
            paren_group += paren_string[i]
            paren_list.push(paren_group)
            paren_group = ''
        } else if (paren_string[i] !== ' ') {
            paren_group += paren_string[i]
        }
    }

    return paren_list
}

B:
const separateParenGroups = (paren_string) => {
    const paren_list = []
    let paren_group = ''

    for (let i = 0; i < paren_string.length; i++) {
        if (paren_string[i] === '(') {
            paren_group += paren_string[i]
        } else if (paren_string[i] === ')') {
            paren_group += paren_string[i]
            paren_list.push(paren_group)
            paren_group = ''
        }
    }

    return paren_list
}

C:
const separateParenGroups = (paren_string) => {
    const paren_list = []
    let paren_group = ''

    for (let i = 0; i < paren_string.length; i++) {
        if (paren_string[i] === '(') {
            paren_group += paren_string[i]
        } else if (paren_string[i] === ')') {
            paren_group += paren_string[i]
            paren_list.push(paren_group)
            paren_group = ''
        } else if (paren_string[i] !== ' ') {
            paren_group += par