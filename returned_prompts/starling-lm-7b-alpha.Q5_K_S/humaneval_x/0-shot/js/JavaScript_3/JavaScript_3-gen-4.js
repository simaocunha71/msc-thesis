    let balance = 0;

    operations.forEach(operation => {
        balance += operation;
        if(balance < 0){
            return true;
        }
    });

    return false;
};

console.log(belowZero([1, 2, 3])); //false
console.log(belowZero([1, 2, -4, 5])); //true




/*
