  const regex = /^\d{2}-\d{2}-\d{4}$/;
  if (date === '' || !regex.test(date)) {
    return false;
  }

  const [mm, dd, yyyy] = date.split('-');
  const dateObj = new Date(yyyy, mm - 1, dd);
  return dateObj.getMonth() + 1 == mm && dateObj.getDate() == dd;
}



