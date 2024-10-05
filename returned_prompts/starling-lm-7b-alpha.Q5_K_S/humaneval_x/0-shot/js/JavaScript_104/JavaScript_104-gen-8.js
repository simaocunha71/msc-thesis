    return x.filter(i => !i.toString().match(/[02468]/)).sort((a, b) => a - b);
};

B:
    const arr = [];
    x.forEach(i => {
        const str = i.toString().split('');
        if (!str.some(n => parseInt(n) % 2 === 0)) arr.push(i);
    });
    return arr.sort((a, b) => a - b);
};

C:
    const res = [];
    for (let i = 0; i < x.length; i++) {
        const digits = x[i].toString().split('');
        if (!digits.some(digit => digit % 2 === 0)) {
            res.push(x[i]);
        }
    }
    return res.sort((a, b) => a - b);
};

D:
    const arr = [];
    for (let i = 0; i < x.length; i++) {
        let flag = true;
        const digits = x[i].toString().split('');
        for (let j = 0; j < digits.length; j++) {
            if (parseInt(digits[j]) % 2 === 0) {
                flag = false;
                break;
            }
        }
        if (flag) arr.push(x[i]);
    }
    return arr.sort((a, b) => a - b);
};


























































































































































