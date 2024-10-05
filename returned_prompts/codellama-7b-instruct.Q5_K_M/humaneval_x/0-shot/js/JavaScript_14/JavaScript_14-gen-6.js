  /* Return list of all prefixes from shortest to longest of the input string
    >>> allPrefixes('abc')
    ['a', 'ab', 'abc']
    */
    const allPrefixes = (string) => {
      const prefixes = [];
      for (let i = 0; i < string.length; i++) {
        prefixes.push(string.substring(0, i + 1));
      }
      return prefixes;
    };

