
const validDate = (date) => {
  const dateArr = date.split('-');
  if (
    dateArr.length !== 3 ||
    dateArr[0].length !== 2 ||
    dateArr[1].length !== 2 ||
    dateArr[2].length !== 4 ||
    isNaN(dateArr[0]) ||
    isNaN(dateArr[1]) ||
    isNaN(dateArr[2])
  ) {
    return false;
  }
  const month = parseInt(dateArr[0], 10);
  const day = parseInt(dateArr[1], 10);
  const year = parseInt(dateArr[2], 10);
  if (month < 1 || month > 12) {
    return false;
  }
  if (day < 1 || day > 31) {
    return false;
  }
  if (month === 2 && day > 29) {
    return false;
  }
  if (month % 2 === 0 && (day < 1 || day > 30)) {
    return false;
  }
  if (month % 2 !== 0 && (day < 1 || day > 31)) {
    return false;
  }
  return true;
};

B:

const validDate = (date) => {
  if (typeof date !== 'string') return false;
  const [month, day, year] = date.split('-');
  if (!month || !day || !year) return false;
  if (month < 1 || month > 12) return false;
  if (day < 1 || day > 31) return false;
  if (month === 2 && day > 29) return false;
  if (month % 2 === 0 && (day < 1 || day > 30)) return false;
  if (month % 2 !== 0 && (day < 1 || day > 31)) return false;
  return true;
};

C:

const validDate = (date) => {
  const [month, day, year]