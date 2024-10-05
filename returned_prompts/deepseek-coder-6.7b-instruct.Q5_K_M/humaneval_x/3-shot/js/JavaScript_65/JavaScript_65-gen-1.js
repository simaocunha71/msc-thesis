  const digits = Array.from(String(x), Number);
  if (shift >= digits.length) {
    return digits.reverse().join('');
  } else {
    const shiftDigits = digits.splice(digits.length - shift);
    return [...shiftDigits, ...digits].join('');
  }
}



