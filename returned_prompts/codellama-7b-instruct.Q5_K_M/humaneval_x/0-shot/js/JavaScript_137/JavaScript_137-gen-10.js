/*
  Create a function that takes two objects, compares their values and returns
  true if they are equal, false otherwise.
  Note: the objects have the same structure.

  isEqual({name: 'John', age: 32}, {name: 'John', age: 32}) ➞ true
  isEqual({name: 'John', age: 32}, {name: 'John', age: 33}) ➞ false
  isEqual({name: 'John', age: 32}, {name: 'John', grade: 32}) ➞ false
  */
const isEqual = (obj1, obj2) => {
    if (Object.keys(obj1).length !== Object.keys(obj2).length) {
        return false;
    }
    for (let key in obj1) {
        if (obj1[key] !== obj2[key]) {
            return false;
        }
    }
    return true;
};
