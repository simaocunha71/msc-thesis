const filterIntegers = (values) => values.filter(isInteger);

B:
const filterIntegers = (values) => values.filter(x => typeof x === 'number' && x % 1 === 0);

C:
const filterIntegers = (values) => values.filter(x => Number.isInteger(x));

D:
const filterIntegers = (values) => values.filter(x => typeof x === 'number' && Number.isInteger(x));
