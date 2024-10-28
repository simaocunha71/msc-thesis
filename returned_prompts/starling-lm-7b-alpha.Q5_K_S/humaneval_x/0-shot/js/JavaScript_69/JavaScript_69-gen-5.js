
// We can start by creating a map of the list to count the occurrence of each number
let map = new Map();
lst.forEach(num => {
    if (map.has(num)) {
        map.set(num, map.get(num) + 1);
    }