const f = n => {
let res = [];
for (let i = 1; i <= n; i++) {
if (i % 2 === 0) {
res.push(i * (i - 1) / 2);
} else {
res.push(i * (i + 1) / 2);
}
}
return res;
};
