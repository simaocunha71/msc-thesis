/*Write a function that takes a string and returns true if the string
  length is a prime number or false otherwise
  Examples
  primeLength('Hello') == true
  primeLength('abcdcba') == true
  primeLength('kittens') == true
  primeLength('orange') == false
  */
const primeLength = (string) => {
  if(string.length === 0){return false}else{console.log(string)}
    for(var i=2;i<Math.sqrt(string.length);i++){if(string[i]===' ')break}for(var j=i+1;j<Math.sqrt(string.length);j++){if((string[i] == string[j]) && (string[i] != ' ')&&(i != 0)){return false}}else{return true}
};