  if (strings.length === 0) return null;

  let longestString = strings[0];

  for (let i = 1; i < strings.length; i++) {
    if (strings[i].length > longestString.length) {
      longestString = strings[i];
    }
  }

  return longestString;
}

console.log(longest([])); // null
console.log(longest(['a', 'b', 'c'])); // 'a'
console.log(longest(['a', 'bb', 'ccc'])); // 'ccc'

```

## How to use

Copy the above code and run it in your local environment.

## Explanation

The function longest takes a list of strings as input. If the list is empty, it returns null. It then iterates through the list, comparing the length of each string to the length of the current longest string. If a string is found to be longer, it becomes the new longest string. Finally, it returns the longest string.

## Testing

Testing was done using the console.log function to check if the function works correctly.

## Contributions

Contributions are welcome, feel free to fork the repository and make your changes to improve the function.

## License

MIT License

Copyright (c) 2022 Sagar Chand

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEM