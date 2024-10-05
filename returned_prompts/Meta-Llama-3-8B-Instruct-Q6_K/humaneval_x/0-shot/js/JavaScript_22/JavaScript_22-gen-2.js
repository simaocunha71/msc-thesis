```
const filterIntegers = (values) => values.filter(x => typeof x === 'number' && !isNaN(x) && Math.floor(x) === x);
``` 