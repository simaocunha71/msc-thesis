  let parts = file_name.split('.');
  if (parts.length !== 2) return 'No';
  let prefix = parts[0].replace(/[^a-zA-Z0-9]/g, '');
  if (prefix.length > 0 && !/^[a-zA-Z]+$/.test(prefix)) return 'No';
  if (prefix.length > 3 || /[^a-zA-Z0-9]/g.test(prefix)) return 'No';
  let suffix = parts[1].toLowerCase();
  if (suffix !== 'txt' && suffix !== 'exe' && suffix !== 'dll') return 'No';
  return 'Yes';
} 