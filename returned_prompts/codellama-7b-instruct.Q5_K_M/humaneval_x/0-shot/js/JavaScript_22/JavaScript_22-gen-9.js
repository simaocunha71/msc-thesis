const filterIntegers = (values) => {
  return values.filter((v) => typeof v === 'number' && isFinite(v));
};

B:
const filterIntegers = (values) => {
  return values.filter(v => typeof v === 'number' && isFinite(v));
};

C:
const filterIntegers = (values) => {
  return values.filter(v => v % 1 === 0);
};

D:
const filterIntegers = (values) => {
  return values.filter(v => v !== '' && v !== false && v !== null);
};

E:
const filterIntegers = (values) => {
  return values.filter(v => isFinite(v));
};
