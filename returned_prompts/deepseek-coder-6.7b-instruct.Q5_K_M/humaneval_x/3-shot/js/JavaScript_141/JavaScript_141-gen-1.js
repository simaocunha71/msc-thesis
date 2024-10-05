  let parts = file_name.split('.');
  if  (parts.length  != 2  ||  parts[1]  !=  'txt'  &&  parts[1]  !=  'exe'  &&  parts[1]  !=  'dll')  {
    return "No";
  }
  parts  [0]=  parts[0].replace(/[0-9]/g,  '');
  if  (parts[0]  ==  ''  ||  !isNaN(parts[0][0])  ||  parts[0].match(/[0-9]{4,}/))  {
    return "No";
  }
  return "Yes";
}



