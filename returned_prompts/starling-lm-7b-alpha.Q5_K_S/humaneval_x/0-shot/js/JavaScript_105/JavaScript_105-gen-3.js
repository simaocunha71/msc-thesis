    const arr1 = arr.filter(num => {
        if (num >= 1 && num <= 9) {
            return num;
        }
    });

    arr1.sort(function(a, b) {
        return a - b;
    });

    arr1.reverse();

    const arr2 = arr1.map(function(num) {
        switch (num) {
            case 1:
                return 'One';
            case 2:
                return 'Two';
            case 3:
                return 'Three';
            case 4:
                return 'Four';
            case 5:
                return 'Five';
            case 6:
                return 'Six';
            case 7:
                return 'Seven';
            case 8:
                return 'Eight';
            case 9:
                return 'Nine';
        }
    });
    return arr2;
};

console.log(byLength([1, 2, 3, 4, 5, 6, 7, 8, 9, -1, 100, 11]));








































































































































































































































