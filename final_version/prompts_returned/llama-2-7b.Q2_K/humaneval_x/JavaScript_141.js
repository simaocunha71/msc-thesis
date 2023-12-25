/*Create a function which takes a string representing a file's name, and returns
  'Yes' if the the file's name is valid, and returns 'No' otherwise.
  A file's name is considered to be valid if and only if all the following conditions 
  are met:
  - There should not be more than three digits ('0'-'9') in the file's name.
  - The file's name contains exactly one dot '.'
  - The substring before the dot should not be empty, and it starts with a letter from 
  the latin alphapet ('a'-'z' and 'A'-'Z').
  - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
  Examples:
  fileNameCheck("example.txt") # => 'Yes'
  fileNameCheck("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
  */
const fileNameCheck = (file_name) => {
    if (file_name === '') return false;
    
    if (!!/^(.*?)\.(txt|exe|dll)$/i.test(file_name)) //If it is not a .txt, .exe or .dll file...
        return 'No';
    
    const fileNameSplits = file_name.split('.'), //The function takes the name of the file and splits it by using split(...) method with '.' as delimiter. 
      fileNameBeforeDotSplit = fileNameSplits[0], //The substring before the dot character in the string is taken, and returned as a variable named fileNameBeforeDotSplit.
      fileNameAfterDotSplit = fileNameSplits[1];
    
    if (fileNameBeforeDotSplit === '') return 'No'; //If the substring before the dot character in the file name is not empty...
    
    let fileNameBeforeDotValid = true;
    if (!!/(^[a-zA-Z]+$)/i.test(fileNameBeforeDotSplit))
        fileNameBeforeDotValid = false; //If the substring before the dot character in the file name is NOT empty, ... and it is NOT a letter... 
    
    return (!!/^(txt|exe|dll