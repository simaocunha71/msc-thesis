const willItFly = (q, w) => {
    let weight = 0;
    for (let i = 0; i < q.length; i++) {
        weight += q[i];
    }
    if (q.length === q.reverse().length && weight <= w) {
        return true;
    } else {
        return false;
    }
}

