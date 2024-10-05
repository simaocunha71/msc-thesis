const nextSmallest = (lst) => {
    let min = null;
    let second = null;
    for(let i = 0; i < lst.length; i++) {
        if(min === null) {
            min = lst[i];
        } else if(lst[i] < min) {
            second = min;
            min = lst[i];
        } else if(lst[i] > min && (second === null || lst[i] < second)) {
            second = lst[i];
        }
    }
    return second;
}

