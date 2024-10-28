  const noEvenDigits = n => {
    const str = n.toString();
    for (let i = 0; i < str.length; i++) {
      if (str[i] % 2 === 0) return false;
    }
    return true;
  }

  return x.filter(noEvenDigits).sort((a, b) => a - b);
}



