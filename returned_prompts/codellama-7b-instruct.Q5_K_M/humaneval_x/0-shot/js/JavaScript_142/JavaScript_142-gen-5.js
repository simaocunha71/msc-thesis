const sumSquares = (lst) => {
let result = 0;
for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
        result += Math.pow(lst[i], 2);
    } else if (i % 4 === 0 && i % 3 !== 0) {
        result += Math.pow(lst[i], 3);
    }
}
return result;
};


B:
const sumSquares = (lst) => {
let result = 0;
for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
        result += Math.pow(lst[i], 2);
    } else if (i % 4 === 0 && i % 3 !== 0) {
        result += Math.pow(lst[i], 3);
    }
}
return result;
};


C:
const sumSquares = (lst) => {
let result = 0;
lst.forEach((item, index) => {
    if (index % 3 === 0) {
        result += Math.pow(item, 2);
    } else if (index % 4 === 0 && index % 3 !== 0) {
        result += Math.pow(item, 3);
    }
});
return result;
};


D:
const sumSquares = (lst) => {
let result = 0;
lst.forEach((item, index) => {
    if (index % 3 === 0) {
        result += item * item;
    } else if (index % 4 === 0 && index % 3 !== 0) {
        result += item * item * item;
    }
});
return result;
};


E:
const sumSquares = (lst) => {
let result = 0;
for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
        result += Math.pow(lst[i], 2);
   