const closestInteger = (value) => {
    const rounded = Math.round(value);
    const diffFromRounded = Math.abs(rounded - value);
    const diffFromZero = Math.abs(0 - value);
    if (diffFromRounded < diffFromZero) {
      return rounded;
    }
    return rounded > 0 ? rounded - 1 : rounded + 1;
  };
  
  