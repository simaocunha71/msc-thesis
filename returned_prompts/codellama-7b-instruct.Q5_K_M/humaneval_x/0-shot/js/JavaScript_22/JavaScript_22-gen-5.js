const filterIntegers = (values) => values.filter(e => typeof e === 'number');

B:
const filterIntegers = (values) => values.filter(e => Number.isInteger(e));

C:
const filterIntegers = (values) => values.filter(e => e % 1 === 0);

D:
const filterIntegers = (values) => values.filter(e => Number.isInteger(e) && e > 0);

E:
const filterIntegers = (values) => values.filter(e => e instanceof Number);

F:
const filterIntegers = (values) => values.filter(e => e.constructor === Number);

G:
const filterIntegers = (values) => values.filter(e => typeof e === 'number' && e > 0);

H:
const filterIntegers = (values) => values.filter(e => e % 1 === 0 && e > 0);