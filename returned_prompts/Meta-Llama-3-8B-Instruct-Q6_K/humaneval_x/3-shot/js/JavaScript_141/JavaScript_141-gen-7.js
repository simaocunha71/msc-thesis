  let [beforeDot, afterDot] = file_name.split('.');
  if (beforeDot.length > 0 && /^[a-zA-Z]/.test(beforeDot) && /\d/.test(beforeDot.replace(/[^0-9]/g, '')) <= 3 && ['txt', 'exe', 'dll'].includes(afterDot)) {
    return 'Yes';
  } else {
    return 'No';
  }
}
// Using Regular Expressions
const fileNameCheck = (file_name) => {
  let [beforeDot, afterDot] = file_name.split('.');
  if (/^[a-zA-Z][a-zA-Z0-9]{0,2}/.test(beforeDot) && /^[a-zA-Z0-9]+$/.test(afterDot) && ['txt', 'exe', 'dll'].includes(afterDot)) {
    return 'Yes';
  } else {
    return 'No';
  }
}
// Using ES6 syntax
const fileNameCheck = (file_name) => {
  let [beforeDot, afterDot] = file_name.split('.');
  if (beforeDot.match(/^[a-zA-Z][a-zA-Z0-9]{0,2}$/) && ['txt', 'exe', 'dll'].includes(afterDot)) {
    return 'Yes';
  } else {
    return 'No';
  }
}  // Using a more concise approach
const fileNameCheck = (file_name) => {
  let [beforeDot, afterDot] = file_name.split('.');
  return /^[a-zA-Z][a-zA-Z0-9]{0,2}$/.test(beforeDot) && ['txt', 'exe', 'dll'].includes(afterDot) ? 'Yes' : 'No';
}  // Using a more concise approach with a regular expression
const fileNameCheck = (file_name) => {
  let [beforeDot, afterDot] = file_name.split('.');
  return /^[a-zA-Z][a-zA-Z0-9]{0,2}\.[txt,exe,dll]$/.test(file_name) ? 'Yes' : 'No';
}  // Using a more concise approach with a regular expression and string interpolation
const fileNameCheck = (file_name) => {
  let [beforeDot, afterDot] = file_name.split('.');
  return `${beforeDot}${afterDot}`.match(/^[a-zA-Z][a-zA-Z0-9]{0,2}\.[txt,exe,dll]$/) ? 'Yes' : 'No';
}
// Using