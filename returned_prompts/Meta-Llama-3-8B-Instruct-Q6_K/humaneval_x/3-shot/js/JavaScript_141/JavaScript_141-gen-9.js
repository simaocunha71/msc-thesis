  let [beforeDot, afterDot] = file_name.split('.');
  let hasDigit = /\d/.test(beforeDot);
  let invalidBeforeDot = !beforeDot.match(/^[a-zA-Z]/);
  let invalidAfterDot = !['txt', 'exe', 'dll'].includes(afterDot);
  let hasMoreThanThreeDigits = /\d{4}/.test(beforeDot);
  
  return !hasDigit && !invalidBeforeDot && !invalidAfterDot && !hasMoreThanThreeDigits ? 'Yes' : 'No';
}