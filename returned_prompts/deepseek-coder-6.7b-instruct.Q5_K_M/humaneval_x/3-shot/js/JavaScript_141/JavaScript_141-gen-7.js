  const valid_extensions 
  = ['txt', 'exe', 'dll'];
  const extension_index 
  = file_name.lastIndexOf('.');
  const name_part 
  = file_name.slice(0, extension_index);
  const extension_part 
  = file_name.slice(extension_index + 1);

  if  (/\d{4,}/.test(file_name)) 
  {
    return 'No';
  }
  else if  (!(/[a-zA-Z].*[.]/.test(file_name))) 
  {
    return 'No';
  }
  else if  (!valid_extensions.includes(extension_part)) 
  {
    return 'No';
  }
  else if  (name_part.includes('.') 
  || name_part === '') 
  {
    return 'No';
  }
  else 
  {
    return 'Yes';
  }
}



