One liner solution:
  function compareOne(a, b) {
    return (typeof a === 'string' && typeof b === 'string') ?
      (parseFloat(a) > parseFloat(b) ? a : b) :
      (a > b ? a : b);
  }


Two liner solution:
function compareOne(a, b) {
  return (typeof a === 'string' && typeof b === 'string') ?
    (parseFloat(a) > parseFloat(b) ? a : b) :
    (a > b ? a : b);
}


Multi liner solution:

function compareOne(a, b) {
  let aType = typeof a;
  let bType = typeof b;
  if (aType === 'string' && bType === 'string') {
    return parseFloat(a) > parseFloat(b) ? a : b;
  } else if (aType === 'string' && bType === 'number') {
    return parseFloat(a) > b ? a : b;
  } else if (aType === 'number' && bType === 'string') {
    return a > parseFloat(b) ? a : b;
  } else if (aType === 'number' && bType === 'number') {
    return a > b ? a : b;
  }
  return null;
}


*/

























































































































































































