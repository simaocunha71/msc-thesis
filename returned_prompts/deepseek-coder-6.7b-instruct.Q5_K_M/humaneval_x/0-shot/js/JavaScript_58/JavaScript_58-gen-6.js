
    const set1 = new Set(l1);
    const set2 = new Set(l2);

    const commonSet = new Set([...set1].filter(x => set2.has(x)));

    return Array.from(commonSet).sort((a, b) => a - b);

}

module.exports = common;

/*
