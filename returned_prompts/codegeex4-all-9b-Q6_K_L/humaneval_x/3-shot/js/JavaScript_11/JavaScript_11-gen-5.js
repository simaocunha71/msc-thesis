  var result = '';
  for (let i = 0; i < Math.max(a.length, b.length); i++) {
    var a_bit = a[i] ? 1 : 0;
    var b_bit = b[i] ? 1 : 0;
    var xor_bit = (a_bit ^ b_bit) ? '1' : '0';
    result += xor_bit;
  }
  return result;
}



