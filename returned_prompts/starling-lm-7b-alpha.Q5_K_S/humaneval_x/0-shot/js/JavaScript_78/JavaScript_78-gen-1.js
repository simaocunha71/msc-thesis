    let arr = [];
    let num1 = num.split('');
    if (num.length === 0) {
        return 0;
    }
    let num2 = [];
    for (let i = 0; i < num1.length; i++) {
        if (num1[i] >= '0' && num1[i] <= '9') {
            num2.push(Number(num1[i]));
        } else {
            switch (num1[i]) {
                case 'A':
                    num2.push(10);
                    break;
                case 'B':
                    num2.push(11);
                    break;
                case 'C':
                    num2.push(12);
                    break;
                case 'D':
                    num2.push(13);
                    break;
                case 'E':
                    num2.push(14);
                    break;
                case 'F':
                    num2.push(15);
                    break;
            }
        }
    }
    num2.forEach(elem => {
        if (elem > 1) {
            for (let i = 2; i <= Math.sqrt(elem); i++) {
                if (elem % i === 0) {
                    return;
                }
            }
            arr.push(elem);
        }
    });
    return arr.length;
};

console.log(hexKey("ABED1A33"));

*/











































































































































