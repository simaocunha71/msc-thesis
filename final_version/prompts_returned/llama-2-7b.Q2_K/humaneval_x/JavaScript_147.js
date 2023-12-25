/*
  You are given a positive integer n. You have to create an integer array a of length n.
      For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
      Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
  and a[i] + a[j] + a[k] is a multiple of 3.

  Example :
      Input: n = 5
      Output: 1
      Explanation: 
      a = [1, 3, 7, 13, 21]
      The only valid triple is (1, 7, 13).
  */
const getMaxTriples = (n) => {
    let arr = [];
    for(let i=0;i<n+1;i++){
        if(!Array.isArray(arr[i-1]) && !(Array.isArray(arr[i-1])&&!arr[i-1].length)){
            let triple = Array.from({ length: n })
            for(let j=0;j<n+1;j++){
                if(!triple.includes(`${i}`) && !triple.includes(`${j}`) ){
                    triple[triple.length]=`${i}`,triple[triple.length]=i*i-i+1;
                }
            }
        arr.push(triple)
    }
    return n
};
module.exports = getMaxTriples