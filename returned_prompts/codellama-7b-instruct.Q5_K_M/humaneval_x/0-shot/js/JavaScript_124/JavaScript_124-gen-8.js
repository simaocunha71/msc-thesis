/*
  const validDate = (date) => {
    if(date.length === 0) return false;
    let month = date.slice(0,2);
    let day = date.slice(3,5);
    let year = date.slice(6,10);

    if(month < 1 || month > 12) return false;
    if(day < 1 || day > 31) return false;
    if(year < 1970 || year > 2050) return false;

    return true;
  }
*/
  const validDate = (date) => {
    if(date.length === 0) return false;
    let [month, day, year] = date.split('-');

    if(month < 1 || month > 12) return false;
    if(day < 1 || day > 31) return false;
    if(year < 1970 || year > 2050) return false;

    return true;
  }

  const validDate = (date) => {
    const [month, day, year] = date.split('-');
    if(month < 1 || month > 12) return false;
    if(day < 1 || day > 31) return false;
    if(year < 1970 || year > 2050) return false;
    return true;
  }

  const validDate = (date) => {
    const [month, day, year] = date.split('-');
    if(month < 1 || month > 12) return false;
    if(day < 1 || day > 31) return false;
    if(year < 1970 || year > 2050) return false;
    return true;
  }

  const validDate = (date) => {
    const [month, day, year] = date.split('-');
    if(month < 1 || month > 12) return false;
    if(day < 1 || day > 31) return false;
    if(year < 