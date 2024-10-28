let newMessage = '';
   for(let i = 0; i < message.length; i++){
     let char = message[i];
     if(/[a-z]/.test(char)){
       if(char === char.toLowerCase()){
         newMessage += char.toUpperCase();
       }else{
         newMessage += char.toLowerCase();
       }
     }else{
       if(char === 'a'){
         newMessage += 'C';
       }else if(char === 'e'){
         newMessage += 'G';
       }else if(char === 'i'){
         newMessage += 'K';
       }else if(char === 'o'){
         newMessage += 'Q';
       }else if(char === 'u'){
         newMessage += 'W';
       }else if(char === 'A'){
         newMessage += 'C';
       }else if(char === 'E'){
         newMessage += 'G';
       }else if(char === 'I'){
         newMessage += 'K';
       }else if(char === 'O'){
         newMessage += 'Q';
       }else if(char === 'U'){
         newMessage += 'W';
       }else{
         newMessage += char;
       }
     }
   }
   return newMessage;
};

console.log(encode('test')); // 'TGST'
console.log(encode('This is a message')); // 'tHKS KS C MGSSCGG'

*/

// Time: O(n) - we have to go through each character of the string once
// Space: O(n) - in the worst case scenario, we might end up creating a new string that's the same size as the input

// The function works by iterating over the input string character by character. If the character is a letter, it changes its case. If the character is a vowel, it replaces it with the corresponding character in the cipher. If the character is anything else, it leaves it as is.

// This function assumes that the input string is a string of letters (including accented characters), numbers, punctuation, and spaces.