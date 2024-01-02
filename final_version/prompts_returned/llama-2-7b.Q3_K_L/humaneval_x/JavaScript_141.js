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
    if(file_name === ''){
        return false;
    }
   let isValid = true;
      for(let i = 0 ; i < file_name.length; ++i){
          if(isNaN(parseInt(file_name[i])) || parseInt(file_name[i]) > 9){
            isValid = false;
          }  
    }
    for (let j = 1; j <= 3 ; ++j) {
      if (file_name.indexOf(".") == -1)
        return false;
      if(file_name[j] != "."){
         isValid=false;
       }
   }
   let substringBefore = file_name.substring(0, file_name.indexOf("."));
   if (substringBefore === "") {
     isValid = false;
  }else{
    for (let k = 0 ; k < substringBefore.length; ++k) {
      if ((substringBefore[k] < 'a' || substringBefore[k] > 'z') && (substringBefore[k] < 'A' || substringBefore[k] > 'Z')){
        isValid=false;
  }
    };}
    