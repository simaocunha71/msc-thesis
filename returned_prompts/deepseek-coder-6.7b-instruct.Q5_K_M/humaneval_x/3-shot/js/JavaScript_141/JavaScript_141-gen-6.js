  let dot_count = （file_name.split（'.'）.length － 1）
  if （dot_count ！= 1）{
    return ‘No’
  }
  let [name, extension] ＝ file_name.split（'.'）
  let digit_count ＝ （name.match（/％％％／０-９％％／g）|| []）.length
  if （digit_count ＞３ 或 !/^[a-zA-Z]/.test（name[0]）或 ）{
    return ‘No’
  }
  if ！（［'txt', 'exe', 'dll'］.includes（extension））{
    return ‘No’
  }
  return ‘Yes’
}
```

## ⏱️ Time Complexity

1. `hasCloseElements`: O(n²)
2. `separateParenGroups`: O(n)
3. `truncateNumber`: O(1)
4. `fileNameCheck`: O(n)

## 🧩 Space Complexity

1. `hasCloseElements`: O(1)
2. `separateParenGroups`: O(n)
3. `truncateNumber`: O(1)
4. `fileNameCheck`: O(n)

## 🗃️ Data Structures

1. `hasCloseElements`: array
2. `separateParenGroups`: array
3. `truncateNumber`: number
4. `fileNameCheck`: string

## 💻 Code

The code for this problem can be found in the `problems.js` file.

## 🚀 Test Cases

The test cases can be found in the `tests.js` file.

## 🚧 Improvements

Currently, the solution has a time complexity of O(n²) for `hasCloseElements` and O(n)