/*Write a function that takes a string and returns true if the string
  length is a prime number or false otherwise
  Examples
  primeLength('Hello') == true
  primeLength('abcdcba') == true
  primeLength('kittens') == true
  primeLength('orange') == false
  */
const primeLength = (string) => {
  if (!string || string.length === 0) {
    throw new Error("Invalid String");
  }
  
  for(var i = 2; i <= string.length; i++) {
    var isPrime = true;
    
    for(var j=1; j<string.length && isPrime;j++){
      if (string[i-1] === string[j]){
        console.log('Error, string is not a prime number');
        throw new Error("String is not a Prime Number");
        break;
      }
    } 
    
    for(var j=0; j<i && isPrime; j++){
      if (string[j] === string[i-1]){
        console.log('Error, string is not a prime number');
        throw new Error("String is not a Prime Number");
        break;
      }
    } 
    
    if(!isPrime) {
      return false;
    } else {
      return true;
    }
}
}