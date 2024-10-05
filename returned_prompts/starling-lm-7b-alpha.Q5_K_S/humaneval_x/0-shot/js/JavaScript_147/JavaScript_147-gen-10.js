    let result = 0;
    let a = [];
    for (let i = 1; i <= n; i++) {
        a.push(i * i - i + 1);
    }
    for (let i = 0; i < a.length; i++) {
        for (let j = i + 1; j < a.length; j++) {
            for (let k = j + 1; k < a.length; k++) {
                if ((a[i] + a[j] + a[k]) % 3 === 0) {
                    result++;
                }
            }
        }
    }
    return result;
};


// Time: O(n^3)
// Space: O(n)

// Test case:
console.log(getMaxTriples(5));


















/*
You are given a positive integer n. You have to create an integer array a of length n.
For each i (1≤i≤n), the value of a[i]=i*i−i+1.
Return the number of triples (a[i],a[j],a[k]) of a where i<j<k,
and a[i]+a[j]+a[k] is a multiple of 3.

Example :
Input: n = 5
Output: 1
Explanation:
a = [1, 3, 7, 13, 21]
The only valid triple is (1, 7, 13).

Correct Solution:

    const getMaxTriples = (n) => {
        let result = 0;
        let a = [];
        for (let i = 1; i <= n; i++) {
            a.push(i * i - i + 1);
        }
        for (let i = 0; i < a.length; i++) {
            for (let j = i + 1; j < a.length; j++) {
                for (let k = j + 1; k < a.length; k++) {
                    if ((a[i