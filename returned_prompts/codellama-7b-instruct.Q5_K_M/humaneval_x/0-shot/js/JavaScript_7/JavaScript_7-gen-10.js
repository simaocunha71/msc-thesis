const filterBySubstring = (strings, substring) => {
strings.filter((string) => string.includes(substring))
}

B:
const filterBySubstring = (strings, substring) => {
strings.filter((string) => string.indexOf(substring) !== -1)
}

C:
const filterBySubstring = (strings, substring) => {
strings.filter((string) => string.match(substring))
}

D:
const filterBySubstring = (strings, substring) => {
strings.filter((string) => string.includes(substring))
}
