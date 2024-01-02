/*
  Write a function that takes a message, and encodes in such a 
  way that it swaps case of all letters, replaces all vowels in 
  the message with the letter that appears 2 places ahead of that 
  vowel in the english alphabet. 
  Assume only letters. 
  
  Examples:
  >>> encode('test')
  'TGST'
  >>> encode('This is a message')
  'tHKS KS C MGSSCGG'
  */
const encode = (message) => {
    let string = message.split("");
    let tempString="";
    for(let i=0; i<string.length;i++)
    {
        tempString += string[i].toUpperCase();
        
        if((i+1)>2 && (tempString[i]==letter.toLowerCase()) ){
            tempString = tempString.replace(letter,letter + letter); 
            tempString = tempString.split("");
            for (let j=0;j<tempString.length;j++)
            {
                if((j+2)>4 && (tempString[j]==letter.toUpperCase()) ){
                    tempString[j]=letter + letter; 
                }
            }
        }
        
    }
    for(let i=0; i<string.length;i++)
    {
        string[i] = tempString[i];    
    }
   return string.join("");
}