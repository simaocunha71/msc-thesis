const fruitDistribution = (s, n) => {
    const [apples, oranges] = s.split(' and ').map(e => +e.split(' ')[0]);
    return n - apples - oranges;
};





