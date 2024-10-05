  let parts = file_name.split('.');
  if (parts.length != 2) return 'No';
  let beforeDot = parts[0];
  let afterDot = parts[1];
  
  if (!/^[a-zA-Z]/.test(beforeDot)) return 'No';
  if (beforeDot.length > 1 && /\d/.test(beforeDot[1])) return 'No';
  if (afterDot.length > 3 && /\d/.test(afterDot[3])) return 'No';
  if (!['txt', 'exe', 'dll'].includes(afterDot)) return 'No';
  return 'Yes';
}