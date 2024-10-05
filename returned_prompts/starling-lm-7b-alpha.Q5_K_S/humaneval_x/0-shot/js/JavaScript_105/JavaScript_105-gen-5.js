    //sort the arr
    arr.sort((a, b) => {
        return a - b;
    });

    //reverse the arr
    arr.reverse();

    //replace each digit by its corresponding name
    let result = [];
    for(let i = 0; i < arr.length; i++) {
        if(arr[i] >= 1 && arr[i] <= 9) {
            result.push(getName(arr[i]));
        }
    }

    return result;
};

const getName = (num) => {
    if(num == 1) {
        return "One";
    } else if(num == 2) {
        return "Two";
    } else if(num == 3) {
        return "Three";
    } else if(num == 4) {
        return "Four";
    } else if(num == 5) {
        return "Five";
    } else if(num == 6) {
        return "Six";
    } else if(num == 7) {
        return "Seven";
    } else if(num == 8) {
        return "Eight";
    } else if(num == 9) {
        return "Nine";
    } else {
        return "";
    }
}

console.log(byLength([2, 1, 1, 4, 5, 8, 2, 3]));
console.log(byLength([1, -1, 55]));
console.log(byLength([]));

*/
