
// Count the number of times 'I' appears in the string
const I_COUNT = S.split('.').filter(sentence => sentence.startsWith('I')).length

// If I_COUNT is greater than 0, return the number of sentences
return I_COUNT > 0 ? S.split('.').length : 0

}

B:

// Get an array of sentences
const sentences = S.split('.')

// Count the number of sentences that start with 'I'
const I_COUNT = sentences.filter(sentence => sentence.startsWith('I')).length

// If I_COUNT is greater than 0, return the number of sentences
return I_COUNT > 0 ? sentences.length : 0
