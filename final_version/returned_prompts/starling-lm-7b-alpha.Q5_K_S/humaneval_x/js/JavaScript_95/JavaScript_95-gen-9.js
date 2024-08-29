  let keys = Object.keys(dict);
  let values = Object.values(dict);
  let result = true;

  keys.forEach(key => {
    if (key.length != 1 || (key != key.toUpperCase() && key != key.toLowerCase())) {
      result = false;
    }
  });

  return result;
}



