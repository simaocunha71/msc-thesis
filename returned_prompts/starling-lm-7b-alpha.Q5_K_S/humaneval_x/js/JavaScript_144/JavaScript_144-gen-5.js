  let [numX, denX] = x.split('/');
  let [numN, denN] = n.split('/');

  let lcm = (denX * denN) / gcd(denX, denN);
  let newNumX = (numX * lcm / denX);
  let newNumN = (numN * lcm / denN);

  if (newNumX % newNumN == 0) {
    return true;
  } else {
    return false;
  }
}

function gcd(a, b) {
  if (b == 0) {
    return a;
  }
  return gcd(b, a % b);
}



