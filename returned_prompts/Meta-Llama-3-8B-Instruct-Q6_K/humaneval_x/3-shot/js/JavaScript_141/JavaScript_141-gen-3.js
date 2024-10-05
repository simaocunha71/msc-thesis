  let [beforeDot, afterDot] = file_name.split('.');
  if (beforeDot.length > 0 && /^[a-zA-Z]/.test(beforeDot) && afterDot.length <= 3 && /^[a-zA-Z0-9]+$/.test(afterDot)) {
    let digits = beforeDot.replace(/[^0-9]/g, '').length;
    return digits <= 3 ? 'Yes' : 'No';
  } else {
    return 'No';
  }
}
// Explanation:
// We split the file name into two parts, before and after the dot.
// We check if beforeDot is not empty, starts with a letter, and afterDot has length less than or equal to 3 and only contains letters and digits.
// Then we check if there are more than 3 digits in beforeDot and return 'Yes' or 'No' accordingly. If the conditions are not met, we return 'No'.