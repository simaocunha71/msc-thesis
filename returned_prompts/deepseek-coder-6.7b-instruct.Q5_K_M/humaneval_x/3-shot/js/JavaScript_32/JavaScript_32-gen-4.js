  let start = 0.0, end = 1.0;
  while  (poly(xs, start) * poly(xs, end) > 0.0) {
    if  (Math.abs(poly(xs, start)) < Math.abs(poly(xs, end))) {
      start  *= 2.0;
      end  *= 2.0;
     } else {
      start  /= 2.0;
      end  /= 2.0;
     }
   }
   while  (Math.abs(end  - start) > 1e-6) {
    let mid = (start  + end ) / 2.0;
    if  (poly(xs, mid)  * poly(xs, start)  < 0.0) {
      end  =  mid;
     } else {
      start  =  mid;
     }
   }
  return start;
}



