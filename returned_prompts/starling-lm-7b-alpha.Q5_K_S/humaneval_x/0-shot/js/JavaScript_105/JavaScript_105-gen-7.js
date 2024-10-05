    const result = [];

    for (let i = 0; i < arr.length; i++) {
      if (arr[i] >= 1 && arr[i] <= 9) {
        result.push(arr[i]);
      }
    }

    result.sort((a, b) => {
      return a - b;
    });

    result.reverse();

    const names = {
      1: "One",
      2: "Two",
      3: "Three",
      4: "Four",
      5: "Five",
      6: "Six",
      7: "Seven",
      8: "Eight",
      9: "Nine"
    };

    const namesArray = [];

    for (let i = 0; i < result.length; i++) {
      namesArray.push(names[result[i]]);
    }

    return namesArray;

};

module.exports = byLength;

*/

/*

const arr = [2, 1, 1, 4, 5, 8, 2, 3];
const result = byLength(arr);
console.log(result);

const arr2 = [];
const result2 = byLength(arr2);
console.log(result2);

const arr3 = [1, -1 , 55];
const result3 = byLength(arr3);
console.log(result3);

*/

































































































































































