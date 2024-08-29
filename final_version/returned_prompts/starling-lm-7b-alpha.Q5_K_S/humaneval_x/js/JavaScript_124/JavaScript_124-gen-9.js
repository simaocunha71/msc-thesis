  const [month, day, year] = date.split('-');
  return (
    date.length > 0 &&
    month.length === 2 &&
    day.length === 2 &&
    year.length === 4 &&
    month <= 12 && month >= 1 &&
    day <= 31 && (month === '02' ? day <= 29 : (month === '01' || month === '03' || month === '05' || month === '07' || month === '08' || month === '10' || month === '12' ? day <= 31 : day <= 30)) &&
    year.length === 4
  );
}



