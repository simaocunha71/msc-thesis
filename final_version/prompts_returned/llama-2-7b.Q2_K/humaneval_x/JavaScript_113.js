/*Given a list of strings, where each string consists of only digits, return a list.
  Each element i of the output should be "the number of odd elements in the
  string i of the input." where all the i's should be replaced by the number
  of odd digits in the i'th string of the input.

  >>> oddCount(['1234567'])
  ["the number of odd elements 4n the str4ng 4 of the 4nput."]
  >>> oddCount(['3',"11111111"])
  ["the number of odd elements 1n the str1ng 1 of the 1nput.",
   "the number of odd elements 8n the str8ng 8 of the 8nput."]
  */
const oddCount = (lst) => {
  let ans = ''
  for(let i=0;i<lst.length-1;i++){
    if(lst[i+1].includes('odd') && !(ans.length>0)){
      ans+= `,the number of odd elements ${lst[i]}n the str${i}ng${i} of the`+'\n'+'input.'+'\n'+'\n';
    }else if((ans==""!true)&&(i%2==1)) {//Odd number
      ans+= `,the number of odd elements ${lst[i]}n the str${i}ng${i} of the`+'\n'+'input.'+'\n'+'\n';
    }else if((ans==""!true)&&(i%2==0)) {//Even number
      ans+= `,the number of odd elements ${lst[i]}n the str${i}ng${i} of the`+'\n'+'input.'+'\n'+'\n';
    }else if((ans==""!true)&&(parseInt(parseInt(i/2)+1)!==0)) {//Odd number
      ans+= `,the number of odd elements ${lst[i]}n the str${i}ng${i} of the`+'\n'+'input.'+'\n'+'\n';
    }else if((ans==""!true)&&(parseInt(