const strangeSortList = (lst) => {
lst.sort((a, b) => a - b);
let result = [];

result.push(lst[0]);
result.push(lst[lst.length - 1]);

for (let i = 1; i < lst.length - 1; i += 2) {
result.push(lst[i]);
}

for (let i = 0; i < lst.length - 1; i += 2) {
result.push(lst[i]);
}

return result;
}

B:
const strangeSortList = (lst) => {
lst.sort((a, b) => a - b);
let result = [];

for (let i = 0; i < lst.length; i += 2) {
result.push(lst[i]);
}

for (let i = 1; i < lst.length; i += 2) {
result.push(lst[i]);
}

return result;
}

C:
const strangeSortList = (lst) => {
lst.sort((a, b) => a - b);
let result = [];
let half = lst.length / 2;

for (let i = 0; i < half; i++) {
result.push(lst[i]);
}

for (let i = half; i < lst.length; i++) {
result.push(lst[i]);
}

return result;
}

D:
const strangeSortList = (lst) => {
lst.sort((a, b) => a - b);
let result = [];
let mid = lst.length / 2;

for (let i = 0; i < mid; i++) {
result.push(lst[i]);
}

for (let i = mid; i < lst.length; i++) {
result.push(lst[i]);
}

return result;
}

E:
const strangeSortList = (lst) => {
lst.sort((a, b) => a - b);
let result = [];

for (let i = 0; i < lst.length; i += 2)