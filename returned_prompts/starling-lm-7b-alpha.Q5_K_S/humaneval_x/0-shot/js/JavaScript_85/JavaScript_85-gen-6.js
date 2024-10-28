const sum = lst.filter((num, index) => index % 2 === 0 && num % 2 === 0).reduce((acc, cur) => acc + cur, 0);
return sum;
};

