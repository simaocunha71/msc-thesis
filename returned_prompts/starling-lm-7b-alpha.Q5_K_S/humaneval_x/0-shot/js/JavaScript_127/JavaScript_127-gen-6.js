/*

1) if the start of interval 1 is greater than the end of interval 2, or vice versa, then there is no intersection.
2) calculate the length of the intersection by subtracting the start of the second interval from the end of the first interval.
3) if the length is 0, then there is no intersection.
4) if the length of intersection is a prime number, return 'YES', otherwise return 'NO'.


The time complexity of the solution is O(1) since we only do constant time operations regardless of the size of the input.
The space complexity is also O(1) since we only use constant amount of space regardless of the size of the input.

*/

let s1 = interval1[0];
let e1 = interval1[1];
let s2 = interval2[0];
let e2 = interval2[1];

if(s1 > e2 || s2 > e1){
    return "NO";
}

let length = e1 - s2;

if(length === 0){
    return "NO";
}

for(let i = 2; i <= Math.sqrt(length); i++){
    if(length % i === 0){
        return "NO";
    }
}
return "YES";
};

console.log(intersection((-3, -1), (-5, 5)));

*/



























































































































































































