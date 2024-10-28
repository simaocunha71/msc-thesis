  let maxStrength = -Infinity;
  let strongestExtension = '';

  for (let ext of extensions) {
      let strength = ext.split('').reduce((acc, char) => {
          if (char === char.toUpperCase()) return acc + 1;
          if (char === char.toLowerCase()) return acc - 1;
          return acc;
      }, 0);

      if (strength > maxStrength) {
          maxStrength = strength;
          strongestExtension = ext;
      }
  }

  return `${class_name}.${strongestExtension}`;
}


console.log(strongestExtension('my_class', ['AA', 'Be', 'CC']));  // 'my_class.AA'
console.log(strongestExtension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']));  // 'Slices.SErviNGSliCes'

// Time complexity: O(n*m), where n is the number of extensions and m is the length of the longest extension
// Space complexity: O(1), since we're only storing a constant number of variables.

// The function works by iterating over each extension in the list. For each extension, it calculates the strength by iterating over each character in the extension and checking if the character is uppercase or lowercase. If it's uppercase, it adds 1 to the strength, if it's lowercase, it subtracts 1. The function then compares this calculated strength to the current maximum strength. If the calculated strength is greater, it updates the maximum strength and the strongest extension. Finally, it returns the class name and the strongest extension in the format 'ClassName.StrongestExtensionName'.

// The time complexity of the function is O(n*m) because we're iterating over each extension and each character in the extension. The space complexity is O(1) because we're only storing a constant number of variables.

// The test cases confirm that the function is working correctly by returning the expected output for the input examples.

// This solution assumes that the input will always be valid, i.e., a string and a list