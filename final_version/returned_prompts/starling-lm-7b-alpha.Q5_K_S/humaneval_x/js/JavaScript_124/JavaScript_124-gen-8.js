  const months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"];
  const parts = date.split('-');
  if (parts.length != 3) return false;
  const month_index = months.indexOf(parts[0]);
  if (month_index == -1) return false;
  if (parts[1] == '00' || parts[2] == '0000') return false;
  const number_of_days = parseInt(parts[1]);
  const number_of_month = parseInt(parts[0]);
  if (number_of_days < 1 || number_of_days > 31 && number_of_month < 3 && number_of_month > 11) return false;
  if (number_of_days < 1 || number_of_days > 30 && (number_of_month == 4 || number_of_month == 6 || number_of_month == 9 || number_of_month == 11)) return false;
  if (number_of_days < 1 || number_of_days > 29 && number_of_month == 2) return false;
  return true;
}



