    // The first one is the most obvious one.
    // We'll use a simple loop to iterate through the characters
    // and perform the XOR operation.
    // The loop will be executed at most 100 times, since the inputs
    // are at most 100 characters long.
    var i int
    for i = 0; i < 100; i++ {
        // The XOR operation is simple, just check the value of the
        // characters and return the corresponding result.
        if a[i] != b[i] {
            // If the characters are not equal, return the result.
            return a[i : i+1] + b[i : i+1]
        }
    }

    // If the loop completes without returning anything,
    // it means that the characters are equal,
    // so we just return an empty string.
    return ""
}

// >>> StringXor('010', '110')
// '100'

// >>> StringXor('100', '000')
// '100'

// >>> StringXor('111', '001')
// '110'

// >>> StringXor('101', '011')
// '110'

// >>> StringXor('110', '010')
// '100'

// >>> StringXor('100', '100')
// ''

// >>> StringXor('000', '000')
// ''

// >>> StringXor('111', '111')
// ''

// >>> StringXor('010', '010')
// ''

// >>> StringXor('101', '101')
// ''

// >>> StringXor('001', '001')
// ''

// >>> StringXor('110', '110')
// ''

// >>> StringXor('101', '101')
// ''

// >>> StringXor('111', '111')
// ''
