const splitWords = (txt) => {
  return txt.split(/\s+/);
};

B:
const splitWords = (txt) => {
  return txt.split(/\s+/).filter(x => x.length > 0);
};

C:
const splitWords = (txt) => {
  return txt.split(/\s+/).filter(Boolean);
};

D:
const splitWords = (txt) => {
  return txt.match(/[a-zA-Z]+/g) || [];
};