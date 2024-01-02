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
    let res = 0;
    for(let i=1; i<Math.min(n-1, n-2);i++){ // loop until n - 1 or n - 2
        if(i*i - i + 1 % 3 === 0) {
            let sum = getSumOfArray(a, i);
            res += (sum / 3).toFixed(0);
        }
    }
    return res; // getMaxTriples(n) is the number of triples (a[i], a[j], a[k]) where 1 <= j < k and (a[i] + a[j] + a[k]) is multiple of 3.
};

const getSumOfArray = (arr, i) => {
    let sum = 0;
    for(let j=1; j< Math.min(arr.length - 1, arr.length - 2);j++){ // loop until arr.length - 1 or arr.length - 2
        if(i*j <= arr.length - 1 && i + j <= arr.length) { sum += (getNumber(i+j) - getNumber(i) * (Math.pow(j, i)/Math.pow(i*(i-1), i)))}
    }
    return sum; // sum all the triples in an array.
}

const getNumber = function