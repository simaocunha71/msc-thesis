const moveOneBall = (arr) => {
    if (arr.length === 0) return true;
    if (arr.length === 1) return true;

    let min = 0;
    let max = 0;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] < arr[min]) {
            min = i;
        }
        if (arr[i] > arr[max]) {
            max = i;
        }
    }
    if (min === 0 && max === arr.length - 1) {
        return true;
    }
    if (max === arr.length - 1 && min === 0) {
        return true;
    }

    return false;
}
