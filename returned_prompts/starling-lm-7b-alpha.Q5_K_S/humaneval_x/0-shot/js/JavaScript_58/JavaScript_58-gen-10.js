    const map = {};
    l1.forEach(el => {
        if (!map[el]) map[el] = true;
    });
    l2.forEach(el => {
        if (map[el]) map[el] = true;
    });
    const keys = Object.keys(map).filter(el => map[el]);
    return keys.sort();
}


/*
Given a string, return a sorted list of unique characters.

  >>> sortUnique('hello')
  ["d", "e", "h", "l", "o"]
  >>> sortUnique('world')
  ["d", "l", "o", "r", "w"]

  */
const sortUnique = str => {
    const map = {};
    for (let i = 0; i < str.length; i++) {
        if (!map[str[i]]) map[str[i]] = true;
    }
    return Object.keys(map).sort();
}


/*
Find the first element of a string that matches a pattern.

  >>> matchFirst('hello', 'o')
  "o"
  >>> matchFirst('goodbye', 'b')
  "b"
  >>> matchFirst('goodbye', 'z')
  undefined

  */
const matchFirst = (str, pattern) => {
    for (let i = 0; i < str.length; i++) {
        if (str[i] === pattern) return str[i];
    }
    return undefined;
}


/*
Return the first element in a string that matches a pattern.

  >>> firstMatch('hello', 'o')
  "o"
  >>> firstMatch('goodbye', 'b')
  "b"
  >>> firstMatch('goodbye', 'z')
  undefined

  */
const firstMatch = (str, pattern) => {
    for (let i = 0; i < str.length; i++) {
        if (str[i] === pattern) return str[i];
    }
    return undefined;
}


/*
Return a list of all elements in a string that match a pattern.

  >>> allMatches('hello