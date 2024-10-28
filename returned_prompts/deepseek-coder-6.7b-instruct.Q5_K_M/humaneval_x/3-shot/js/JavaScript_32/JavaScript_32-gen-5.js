  let start 
    = Math.max(...xs.map((c, i) 
    => i % 2 === 0 ? c / xs[xs.length - 1] : - c / xs[xs.length - 1]));
  let end 
    = Math.min(...xs.map((c, i) 
    => i % 2 === 0 ? - c / xs[xs.length - 1] : c / xs[xs.length - 1]));

  while  (true)  {
    let mid 
      = (start + end) / 2.0;
    if  (Math.abs(poly(xs, mid)) < 0.000001)  {
      return mid;
    } 
    if  (poly(xs, start) * poly(xs, mid) < 0)  {
      end = mid;
    } 
    else  {
      start = mid;
    }
  }
}


