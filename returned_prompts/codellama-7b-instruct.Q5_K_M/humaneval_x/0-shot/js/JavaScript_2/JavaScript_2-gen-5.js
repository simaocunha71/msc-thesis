const truncateNumber = (number) => {
    return number % 1;
}

B:
const truncateNumber = (number) => {
    const integerPart = Math.floor(number);
    return number - integerPart;
}

C:
const truncateNumber = (number) => {
    return number - parseInt(number);
}

D:
const truncateNumber = (number) => {
    return number.toString().split('.')[1];
}
