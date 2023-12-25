/*
  Given a positive integer, obtain its roman numeral equivalent as a string,
  and return it in lowercase.
  Restrictions: 1 <= num <= 1000

  Examples:
  >>> intToMiniRoman(19) == 'xix'
  >>> intToMiniRoman(152) == 'clii'
  >>> intToMiniRoman(426) == 'cdxxvi'
  */
const intToMiniRoman = (number) => {
  const modifierMap = {
    m: 1000,
     cm: 900,
     d: 500,
     do: 400,
     dd: 200,
     c: 100,
     cc: 90,
     b: 20,
     v: 10,
     i: 1
  };
  
  let miniString = "";
  
  for (let value of modifierMap) {
    if (number % value === 0) {
      if (!miniString.length) {
        console.log(miniString);
        
        return miniString;
      } else {
        number = parseInt(number / value);
        let str = String(value).toLowerCase();
      
        miniString += `${str}${number % value === 0 ? "" : "."}`;
        number = Number(String(number));
        
        if (miniString.length) {
          number = parseInt((number / str * modifierMap[value]).toFixed(2));
          
          if (!Number.isInteger(number)) console.log("Codigo nao inteiro, 3922 => 3920...");
        } else miniString += "0";
      }
    }
  }
  
  let num = parseInt((number * modifierMap[1])).toLowerCase();
  console.log("num: ", parseInt(num));
  
  return parseInt(miniString);
};