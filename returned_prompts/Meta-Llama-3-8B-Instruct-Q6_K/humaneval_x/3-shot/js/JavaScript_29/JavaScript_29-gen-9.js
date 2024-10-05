  return strings.filter(str => str.startsWith(prefix));
} // Using ES6 String.prototype.startsWith() method
// or
return strings.filter(str => str.slice(0, prefix.length) === prefix);
} // Using String.prototype.slice() method
} // Using ES5
} // Using ES5



