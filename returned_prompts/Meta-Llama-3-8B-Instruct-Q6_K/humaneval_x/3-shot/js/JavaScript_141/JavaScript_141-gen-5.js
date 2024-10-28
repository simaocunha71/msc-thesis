  let parts = file_name.split('.');
  if (parts.length !== 2) return 'No';
  let beforeDot = parts[0];
  let afterDot = parts[1];
  if (!beforeDot.match(/^([a-zA-Z])/)) return 'No';
  if (beforeDot.match(/[0-9]{4,}/)) return 'No';
  let allowedExtensions = ['txt', 'exe', 'dll'];
  if (!allowedExtensions.includes(afterDot)) return 'No';
  return 'Yes';
}