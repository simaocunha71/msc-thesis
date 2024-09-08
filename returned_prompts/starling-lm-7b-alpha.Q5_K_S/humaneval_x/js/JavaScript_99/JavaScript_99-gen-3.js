  const num = parseFloat(value);
  const whole = Math.floor(num);
  const frac = Math.abs(num - whole);
  const sign = Math.sign(num);

  if (frac <= 0.5) {
    return whole * sign;
  }

  return (whole + 1) * sign;
};



