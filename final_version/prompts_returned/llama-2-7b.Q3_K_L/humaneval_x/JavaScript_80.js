/*You are given a string s.
  Your task is to check if the string is happy or not.
  A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
  For example:
  isHappy(a) => false
  isHappy(aa) => false
  isHappy(abcd) => true
  isHappy(aabb) => false
  isHappy(adb) => true
  isHappy(xyy) => false
  */
const isHappy = (s) => {
  let ans = false;
  if(s.length === 2){
    return ans;
  } else{
    for(let i=1,j=2;i<s.length-1;++i,++j){
      if(s[i]===s[i+1]){
        break;
      }
      
      if(s[i]===s[i+1]+s[i+2]){
        ans = true;
        s=s.slice(0,j);
        
        break;
      }
    }
    
  }
  
  return ans;
}
