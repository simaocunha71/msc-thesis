
let num1 = a.toString().split('');
let num2 = b.toString().split('');
let result = 0;

for (let i = 0; i < num1.length; i++) {
    for (let j = 0; j < num2.length; j++) {
        result += (parseInt(num1[i]) * parseInt(num2[j]));
    }
}
return result;
}

