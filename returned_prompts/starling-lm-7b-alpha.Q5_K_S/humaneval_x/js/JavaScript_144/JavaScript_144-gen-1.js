  const [numX, denomX] = x.split('/');
  const [numN, denomN] = n.split('/');

  const num = parseInt(numX) * parseInt(numN);
  const denom = parseInt(denomX) * parseInt(denomN);
  const gcd = (a, b) => {
    return b ? gcd(b, a % b) : a;
  };

  if (num % denom === 0) {
    return num / denom === parseInt(num / denom);
  } else {
    return false;
  }
}



