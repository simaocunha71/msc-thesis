  let length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
}  // ES6 syntax
// or
function primeLength(string) {
  let length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
}  // ES5 syntax
// or
var primeLength = function(string) {
  let length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i * i <= length; i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
};  // ES5 syntax
// or
function primeLength(string) {
  let length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(length); i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
};  // ES5 syntax
// or
var primeLength = function(string) {
  let length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(length); i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
};  // ES5 syntax
// or
function primeLength(string) {
  let length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i <= Math.sqrt(length); i++) {
    if (length % i === 0) {
      return false;
    }
  }
  return true;
};  // ES5 syntax
// or
var primeLength = function(string) {
  let length = string.length;
  if (length <= 1) {
    return false;
  }
  for (let i = 2; i