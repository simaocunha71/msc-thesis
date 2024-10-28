    const months = ['01','03','05','07','08','10','12'];
    const days = ['31'];

    const months2 = ['04','06','09','11'];
    const days2 = ['30'];

    const month = date.slice(0,2);
    const day = date.slice(3,5);
    const year = date.slice(6,10);

    if(month === '02') {
        if(day > 29) {
            return false;
        }
    }

    if(months.includes(month)) {
        if(parseInt(day) > days.length || parseInt(day) > parseInt(days[days.length-1])) {
            return false;
        }
    }

    if(months2.includes(month)) {
        if(parseInt(day) > days2.length || parseInt(day) > parseInt(days2[days2.length-1])) {
            return false;
        }
    }

    if(parseInt(month) < 1 || parseInt(month) > 12) {
        return false;
    }

    if(parseInt(day) < 1 || parseInt(day) > 31) {
        return false;
    }

    if(parseInt(year.length) < 4) {
        return false;
    }

    return true;
};


/*
  Validation Rules
  1. The date string is not empty.
  2. The number of days is not less than 1 or higher than 31 days for months 1,3,5,7,8,10,12. And the number of days is not less than 1 or higher than 30 days for months 4,6,9,11. And, the number of days is not less than 1 or higher than 29 for the month 2.
  3. The months should not be less than 1 or higher than 12.
  4. The date should be in the format: mm-dd-yyyy

  Expected Output:
  validDate('03-1