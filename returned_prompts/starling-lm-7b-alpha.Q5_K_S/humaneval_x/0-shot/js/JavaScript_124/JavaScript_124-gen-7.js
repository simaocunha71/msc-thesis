function validDate(date) {
    if (date === "") {
      return false;
    }
    const dateParts = date.split("-");
    if (dateParts.length !== 3) {
      return false;
    }
    const [month, day, year] = dateParts;
    const monthNumber = parseInt(month, 10);
    const dayNumber = parseInt(day, 10);
    const yearNumber = parseInt(year, 10);
    if (
      monthNumber < 1 ||
      monthNumber > 12 ||
      dayNumber < 1 ||
      (yearNumber % 4 !== 0 && dayNumber > 29) ||
      (yearNumber % 4 === 0 && dayNumber > 29)
    ) {
      return false;
    }
    return true;
  }

  // test
  console.log(validDate('03-11-2000')); // true
  console.log(validDate('15-01-2012')); // false
  console.log(validDate('04-0-2040')); // false
  console.log(validDate('06-04-2020')); // true
  console.log(validDate('06/04/2020')); // false






































































































































































































