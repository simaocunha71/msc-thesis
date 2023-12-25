/*Given a positive integer N, return the total sum of its digits in binary.
  
  Example
      For N = 1000, the sum of digits will be 1 the output should be "1".
      For N = 150, the sum of digits will be 6 the output should be "110".
      For N = 147, the sum of digits will be 12 the output should be "1100".
  
  Variables:
      @N integer
           Constraints: 0 ≤ N ≤ 10000.
  Output:
       a string of binary number
  */
const solve = (N) => {
    let ans = ''
    for(let i=36;i<47;i++){
        const sum = Number(digitsOfBin(N)[i])
        if(!isNaN(sum)){
            ans += String(sum).padStart(2, '0')+i == 110 ? '' : '0'
        }else{
            break
        }
    }
    
    return ans;
}
function digitsOfBin (num) {
    let bin = ''
    const arr = Array.from(new Array(48).fill('0'))
    for(let i=0;i<48;i++){
        if(i>=36 && i<=47){
            arr[i+1]=Number(arr[i])+(num%2)
            bin += parseInt(String(arr[i]).padStart(2, '0') + '')
            
        }else{
            arr[i+1] = num%2 > 0 ? 1 : 0;
            bin+=arr[i+1]==1 ? str(arr[i])+(num%2) == 1 ? '' : '0' : 
                    str(arr[i]) + (num%2)==1 || num%4 >3? '1':'0')
        }
    }
     return bin;
}
function str (n){
    let s = '';
    for(let i=0;i<n.length;i++){s+=(n[i]||