
function largestDivisor(n){
    for(let i = n; i > 1; i--){
        if(n % i === 0) return i;
    }
}

B:

function largestDivisor(n) {
    const factors = [];
    for (let i = 2; i <= n; i++) {
        if (n % i === 0) {
            factors.push(i);
        }
    }
    return factors[factors.length - 1];
}

C:

function largestDivisor(n){
  return n / Math.floor(n/2);
}
