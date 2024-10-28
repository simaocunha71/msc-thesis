const decimalToBinary = (decimal) => {
    let binary = 'db';
    while (decimal > 0) {
        binary = (decimal % 2) + binary;
        decimal = Math.floor(decimal / 2);
    }
    return binary + 'db';
};
