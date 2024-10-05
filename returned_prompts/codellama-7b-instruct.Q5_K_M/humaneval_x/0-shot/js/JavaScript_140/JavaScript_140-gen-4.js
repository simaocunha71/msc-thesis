const fixSpaces = text => text.replace(/\s{2,}/g, '-').replace(/ /g, '_')

B:
const fixSpaces = text => text.replace(/\s+/g, match => match.length > 1 ? '-' : '_')

C:
const fixSpaces = text => text.replace(/[ ]+/g, match => match.length > 1 ? '-' : '_')

D:
const fixSpaces = text => text.replace(/[ ]{2,}/g, '-').replace(/ /g, '_')

E:
const fixSpaces = text => text.replace(/[ ]{2,}/g, '-').replace(/ /g, '_')

F:
const fixSpaces = text => text.replace(/\s{2,}/g, '-').replace(/ /g, '_')

G:
const fixSpaces = text => text.replace(/\s+/g, (match, index) => match.length > 1 ? '-' : (index === 0 ? '' : '_'))

H:
const fixSpaces = text => text.replace(/\s{2,}/g, '-').replace(/ /g, '_')

I:
const fixSpaces = text => text.replace(/\s+/g, (match, index) => match.length > 1 ? '-' : (index === 0 ? '' : '_'))

J:
const fixSpaces = text => text.replace(/\s{2,}/g, '-').replace(/ /g, '_')

K:
const fixSpaces = text => text.replace(/\s+/g, (match, index) => match.length > 1 ? '-' : (index === 0 ? '' : '_'))

L:
const fixSpaces = text => text.replace(/\s{2,}/g, '-').replace(/ /g, '_')

M:
const fixSpaces = text => text.replace(/\s+/g, (match, index) => match.length > 1 ? '-' : (index === 0 ? '' : '_'))

N:
const fixSpaces = text => text.replace(/\s{2,}/