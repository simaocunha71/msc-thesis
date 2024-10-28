while(k--){
  if(arr[k].toString().length<=2)
    A+=arr[k];
  else
    break;
}
return A;

}

B:
while(k--){
  if(arr[k].toString().length<=2)
    return arr.slice(0, k+1).reduce((a,b)=>a+b,0)
  else
    break;
}
return arr.slice(k+1).reduce((a,b)=>a+b,0)

C:
arr.slice(0, k).reduce((a,b)=>a+b,0).filter(num=>num.toString().length<=2).reduce((a,b)=>a+b,0);

D:
arr.slice(0, k).reduce((a,b)=>a+b,0).filter(num=>num.toString().length<=2).length

E:
let sum = 0;
for(let i = 0; i < k; i++){
  if(arr[i].toString().length<=2)
    sum += arr[i];
}
return sum;

F:
return arr.slice(0, k).reduce((a,b)=>a+b,0).filter(num=>num.toString().length<=2).length;


*/





































































































































































































