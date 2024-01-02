/*Write a function that returns true if the given number is the multiplication of 3 prime numbers
  and false otherwise.
  Knowing that (a) is less then 100.
  Example:
  isMultiplyPrime(30) == true
  30 = 2 * 3 * 5
  */
const isMultiplyPrime = (a) => {
    if ((a < 100)) {
        // console.log((a >= 100)); //false
        let prim = []
        for (let i = 2; i <= Math.sqrt(a); i++) {
            if (!prim.includes(i)) {
                prim.push(i)
            }
            
        }
        return prim[0] * prim[1] * prim[2] == a ? true : false; 
    } else {
        return false
    }
}