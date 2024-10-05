const isSorted = (lst) => {
    const sorted = lst.every((v, i, a) => a[i + 1] > v);
    const unique = [...new Set(lst)].length === lst.length;
    return sorted && unique;
};