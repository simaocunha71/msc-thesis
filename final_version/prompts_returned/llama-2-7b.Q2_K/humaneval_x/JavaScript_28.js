/* Concatenate list of strings into a single string
  >>> concatenate([])
  ''
  >>> concatenate(['a', 'b', 'c'])
  'abc'
  */
const concatenate = (strings) => {
  return strings.reduce((result, currentString) => result + currentString, "");
};

/* Concatenate objects into a single object or an array if multiple objects exist
  >>> concatenate({})
  {}
  >>> concatenate([{}, {}, {}])
  [Object, Object, Object]
*/
const concatenateObjects = (objects) => {
  let concatenatedObjects = [];
  for (let i = 0; i < objects.length; i++) {
    const object = objects[i];
    concatenatedObjects.push(object);
  }
  return concatenatedObjects;
};

/* Pulls the first element of an array or throws an error if no elements exist
>>> pull(['a', 'b'])
'a'
>>> pull([])
Error: No data to return!
*/
const pull = (array) => {
  if (!array || !array.length) throw "No data found";

  const firstElement = array[0];
  return firstElement;
};

/* Pulls the only element from an array or throws an error if multiple elements exist
>>> pullObjects(['a', 'b'])
'a'
>>> pullObjects([{}])
Error: No data to return!
*/
const pullObjects = (array) => {
  if (!array || array.length === 1) return array[0];

  throw "Multiple objects in list, no single element selected";
};

/* Replaces the first element of an array or throws an error if no elements exist
>>> replace(['a'], 'c')
'c'
>>> replace([], ['a'])
Error: No data to replace!
*/
const replace = (array, item) => {
  for (let i = 0; i < array.length; i++) {
    if (array[i] === item) return "REPLACED WITH NEW VALUE";
  }
  throw "No data to replace!";
};

/* Rep