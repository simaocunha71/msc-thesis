  function validDate(date){
    const dateRegex = /^(\d{1,2})-(\d{1,2})-(\d{4})$/;
    const match = date.match(dateRegex);
    if(!match){
      return false;
    }
    const month = parseInt(match[1]);
    const day = parseInt(match[2]);
    const year = parseInt(match[3]);
    if(month < 1 || month > 12){
      return false;
    }
    if(day < 1 || day > 31){
      return false;
    }
    if(month === 2){
      if(year % 4 === 0 && year % 100 !== 0){
        if(day < 1 || day > 29){
          return false;
        }
      } else if(day < 1 || day > 28){
        return false;
      }
    } else if(day < 1 || day > 30){
      return false;
    }
    return true;
  }

