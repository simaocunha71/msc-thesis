  const digits = file_name.match(/\d/g);
  const dots = file_name.match(/\./g);
  const txts = file_name.match(/\.txt/g);
  const exes = file_name.match(/\.exe/g);
  const dlls = file_name.match(/\.dll/g);

  if (digits.length > 3 || dots.length != 1 || (txts.length + exes.length + dlls.length) != 1) {
    return 'No';
  } else if (!/[a-zA-Z]/.test(file_name[0])) {
    return 'No';
  } else {
    return 'Yes';
  }
}

// console.log(fileNameCheck("example.txt"));
// console.log(fileNameCheck("1example.dll"));
// console.log(fileNameCheck("example.exe"));
// console.log(fileNameCheck("example.dll"));
// console.log(fileNameCheck("1example.exe"));
// console.log(fileNameCheck("example.1tx"));
// console.log(fileNameCheck("ex1ample.1tx"));
// console.log(fileNameCheck("ex1ample.tx"));
// console.log(fileNameCheck("example.txt1"));

