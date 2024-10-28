function fileNameCheck(file_name) {
  let result = 'Yes';
  if (file_name.length > 3) result = 'No';
  if (file_name.length < 1) result = 'No';
  if (!file_name.includes('.')) result = 'No';
  if (!file_name.charAt(0).match(/[a-zA-Z]/)) result = 'No';
  if (!['txt', 'exe', 'dll'].includes(file_name.slice(-3).toLowerCase())) result = 'No';
  return result;
}

/*
  Test cases:
  console.log(fileNameCheck("example.txt")); // => 'Yes'
  console.log(fileNameCheck("1example.dll")); // => 'No'
  console.log(fileNameCheck("abcde.txt")); // => 'No'
  console.log(fileNameCheck("123abc.txt")); // => 'No'
  console.log(fileNameCheck("abcde.exe")); // => 'No'
  console.log(fileNameCheck("abcde.123")); // => 'No'
  console.log(fileNameCheck("abcde")); // => 'No'
  console.log(fileNameCheck("abcde.txt.")); // => 'No'
  console.log(fileNameCheck("abcde..txt")); // => 'No'
  console.log(fileNameCheck("txt.")); // => 'No'
  console.log(fileNameCheck("123.txt")); // => 'No'
  console.log(fileNameCheck("123abc.exe")); // => 'No'
  console.log(fileNameCheck("123abc.dll")); // => 'No'
  console.log(fileNameCheck("abcde.exe.")); // => 'No'
  console.log(fileNameCheck("abcde..exe")); // => 'No'
  console.log(fileNameCheck("abcde.dll.")); // => 'No'
  console.log(fileNameCheck("abcde..dll")); // => 'No'
  console.log(fileNameCheck("123.exe")); // => 'No'
  console.log(fileName