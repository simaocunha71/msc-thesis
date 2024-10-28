    const arr1 = arr.sort((a, b) => a.length - b.length);

    const arr2 = arr1.reverse();

    const arr3 = arr2.map(item => {
        if (item > 0 && item < 10) {
            switch (item) {
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
                default:
                    break;
            }
        } else {
            return 'One';
        }
    });

    return arr3;
};

module.exports = byLength;
*/

