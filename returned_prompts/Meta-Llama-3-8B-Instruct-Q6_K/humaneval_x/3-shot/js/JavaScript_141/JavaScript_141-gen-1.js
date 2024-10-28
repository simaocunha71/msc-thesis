  const [beforeDot, afterDot] = file_name.split('.');
  if (beforeDot.length > 0 && beforeDot.match(/^([A-Za-z]+)(\d*)$/)) {
    if (afterDot.match(/^(txt|exe|dll)$/)) {
      if (/(\d){4,}/.test(file_name)) {
        return 'No';
      }
      return 'Yes';
    }
  }
  return 'No';
}