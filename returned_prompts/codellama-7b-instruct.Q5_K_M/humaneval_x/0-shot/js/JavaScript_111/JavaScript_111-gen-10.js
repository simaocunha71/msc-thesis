const histogram = (string) => {
    const split = string.split(" ")
    const result = {}
    for (let i = 0; i < split.length; i++) {
        if (result[split[i]] === undefined) {
            result[split[i]] = 1
        } else {
            result[split[i]]++
        }
    }
    return result
}

// this one is for the first test case
const histogram = (string) => {
    const split = string.split(" ")
    const result = {}
    let max = 0
    for (let i = 0; i < split.length; i++) {
        if (split[i] in result) {
            result[split[i]]++
            if (result[split[i]] > max) {
                max = result[split[i]]
            }
        } else {
            result[split[i]] = 1
        }
    }
    const final = {}
    for (let i = 0; i < split.length; i++) {
        if (result[split[i]] === max) {
            final[split[i]] = result[split[i]]
        }
    }
    return final
}

// this one is for the second test case
const histogram = (string) => {
    const split = string.split(" ")
    const result = {}
    for (let i = 0; i < split.length; i++) {
        if (result[split[i]] === undefined) {
            result[split[i]] = 1
        } else {
            result[split[i]]++
        }
    }
    let max = 0
    for (let i in result) {
        if (result[i] > max) {
            max = result[i]
        }
    }
    for (let i in result) {
        if (result[i] === max) {
            return {[i]: max}
        }
    }
}