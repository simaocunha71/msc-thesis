const fixSpaces = (text) => {
  text = text.replace(/\s+/g, (str) => {
    if (str.length > 2) return str.replace(/\s+/g, '-')
    else return '_'
  })
  return text
}

B:
const fixSpaces = (text) => text.replace(/[\s]{2,}/g, '-').replace(/[\s]/g, '_');

C:
function fixSpaces(str) {
  return str.replace(/\s+/g, (match, offset, input) => {
    if (match.length > 2) return '-'
    return '_'
  })
}

D:
function fixSpaces(text) {
  const regex = new RegExp(/\s{2,}/g);
  const replaceChar = '-';
  const result = text.replace(regex, replaceChar);
  return result.replace(/\s/g, '_');
}

E:
const fixSpaces = (text) => text.replace(/\s{2,}/g, '-').replace(/\s/g, '_');

*/
