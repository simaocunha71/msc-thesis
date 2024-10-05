const specialFilter = (nums) => {
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] > 10 && (nums[i].toString()[0] % 2 !== 0 && nums[i].toString()[nums[i].length - 1] % 2 !== 0)) {
            count++;
        }
    }
    return count;
};
*/
