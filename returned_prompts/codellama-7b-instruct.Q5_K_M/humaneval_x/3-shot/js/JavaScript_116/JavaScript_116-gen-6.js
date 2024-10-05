  var count_ones = function(n) {
    return (n & 1) + count_ones(n >> 1);
  }

  return arr.sort(function(a, b) {
    var cnt1 = count_ones(a), cnt2 = count_ones(b);
    if (cnt1 == cnt2) return a - b;
    else return cnt1 - cnt2;
  });
}



