    let min = lst[0];
    let max = lst[0];
    let sorted = [];
    let lstIndex = 1;
    while (lst.length > 0) {
        if (min > lst[lstIndex]) {
            min = lst[lstIndex];
        }
        sorted.push(min);
        lst.splice(lstIndex, 1);
        lstIndex++;

        if (max < lst[lstIndex]) {
            max = lst[lstIndex];
        }
        sorted.push(max);
        lst.splice(lstIndex, 1);
        lstIndex++;
    }
    return sorted;
};

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []

*/

// Using sort() method
function strangeSortList(lst) {
    lst.sort((a, b) => Math.random() - 0.5);
    return lst;
}

console.log(strangeSortList([1, 2, 3, 4])); // [1, 4, 2, 3]
console.log(strangeSortList([5, 5, 5, 5])); // [5, 5, 5, 5]
console.log(strangeSortList([])); // []




































































































































