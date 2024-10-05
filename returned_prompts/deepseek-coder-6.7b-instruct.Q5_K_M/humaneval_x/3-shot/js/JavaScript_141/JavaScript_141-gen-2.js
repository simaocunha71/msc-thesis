  let parts = file_name.split('.');
  if  (parts.length  != 2)  return 'No';
  let [name, ext] = parts;
  if  (!/^[a-zA-Z]/.test(name))  return 'No';
  if  ((name.match(/\d/g) || []).length  >  3)  return 'No';
  if  (!['txt', 'exe', 'dll'].includes(ext))  return 'No';
  return 'Yes';
}



