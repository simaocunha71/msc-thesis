const isSorted = (arr) => {
    if (arr.length === 1) return true;
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) return false;
    }
    return true;
}

B:
const isSorted = (lst) => {
    if (lst.length < 2) return true;
    let prev = lst[0],
        inc = 1;
    for (let i = 1; i < lst.length; i++) {
        if (lst[i] < prev) return false;
        if (lst[i] === prev) inc++;
        prev = lst[i];
    }
    return inc < 2;
}

C:
const isSorted = (lst) => {
    for (let i = 0; i < lst.length - 1; i++) {
        if (lst[i] > lst[i + 1]) return false;
    }
    return true;
}

D:
const isSorted = (lst) => {
    if (lst.length < 2) return true;
    let prev = lst[0],
        inc = 1;
    for (let i = 1; i < lst.length; i++) {
        if (lst[i] < prev) return false;
        if (lst[i] === prev) inc++;
        prev = lst[i];
    }
    return inc < 2;
}

E:
const isSorted = (lst) => {
    const sorted = lst.every((item, index, arr) => {
        if (index === 0) return true;
        return item >= arr[index - 1];
    });
    return sorted && lst.filter((item, index, arr) => item === arr[index - 1]).length < 2;
}
