/*You are given two positive integers n and m, and your task is to compute the
  average of the integers from n through m (including n and m). 
  Round the answer to the nearest integer and convert that to binary.
  If n is greater than m, return -1.
  Example:
  roundedAvg(1, 5) => "0b11"
  roundedAvg(7, 5) => -1
  roundedAvg(10, 20) => "0b1111"
  roundedAvg(20, 33) => "0b11010"
  */
const roundedAvg = (n, m) => {
    let arr = [];
    for (let i = n; i < m; i++) {
        // console.log(`i:${i}`)
        let str = `${i}`;
        if(str == '0') {
            str = 1;
        }
        
        arr[i] = parseInt(str, 2);
    }

    //console.log('arr:', arr)
    var total = 0;
    for (let i of arr) {
        total += i;
    }

    let avg = Math.round(total / arr.length);
    if (avg < 0 || avg > m - n + 1) return -1;

    avg = ((avg * 256).toString(2)).slice(-8);

    return `${avg}`;
}