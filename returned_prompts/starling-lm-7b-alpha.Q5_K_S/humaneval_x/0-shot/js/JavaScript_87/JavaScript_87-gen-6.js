// let arr = [];

for (let i = 0; i < lst.length; i++) {
    for (let j = 0; j < lst[i].length; j++) {
        if (lst[i][j] === x) {
            // arr.push([i, j]);
            yield [i, j];
        }
    }
}

return arr;

};

getRow([
    [1,2,3,4,5,6],
    [1,2,3,4,1,6],
    [1,2,3,4,5,1]
  ], 1) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)];

getRow([], 1) == [];

getRow([[], [1], [1, 2, 3]], 3) == [(2, 2)];




















*/

*/

function* getRow(lst, x) {
    for (let i = 0; i < lst.length; i++) {
        for (let j = 0; j < lst[i].length; j++) {
            if (lst[i][j] === x) {
                yield [i, j];
            }
        }
    }
}

console.log(
    getRow(
        [
            [1,2,3,4,5,6],
            [1,2,3,4,1,6],
            [1,2,3,4,5,1]
        ], 1
    ) == [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]
);

console.log(
    getRow([], 1) == []
);

console.log(
    getRow(
        [[], [1], [1, 2, 3]], 3
    ) == [(2, 2)]
);










