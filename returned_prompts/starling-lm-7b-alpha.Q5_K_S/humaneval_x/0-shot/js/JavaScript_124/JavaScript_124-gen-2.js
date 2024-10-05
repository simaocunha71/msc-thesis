const dateArr = date.split('-');

if (dateArr.length !== 3) return false;

if (dateArr[0].length !== 2 || dateArr[1].length !== 2 || dateArr[2].length !== 4) return false;

if (dateArr[0] < '01' || dateArr[0] > '12') return false;

if (dateArr[1] < '01' || dateArr[1] > '31') return false;

if (dateArr[0] === '02') {
  if (dateArr[1] < '01' || dateArr[1] > '28' || dateArr[1] > '29') return false;
}

if (dateArr[0] === '04' || dateArr[0] === '06' || dateArr[0] === '09' || dateArr[0] === '11') {
  if (dateArr[1] < '01' || dateArr[1] > '30') return false;
}

if (dateArr[0] === '01' || dateArr[0] === '03' || dateArr[0] === '05' || dateArr[0] === '07' || dateArr[0] === '08' || dateArr[0] === '10' || dateArr[0] === '12') {
  if (dateArr[1] < '01' || dateArr[1] > '31') return false;
}

return true;

};












































































































































