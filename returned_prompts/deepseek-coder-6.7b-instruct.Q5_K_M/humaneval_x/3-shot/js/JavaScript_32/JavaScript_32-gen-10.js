  let start  - xs.length / 2;
  let end  - xs.length / 2;

  while  (poly(xs, start)  * poly(xs, end)  >  0)  {
    if  (start  ==  end)  {
      start  -= 0.1;
      end  += 0.1;
     } else  {
      start  += 0.1;
      end  -= 0.1;
     }
   }

  return bisectionMethod(xs, start, end);
}

const bisectionMethod = ((xs, start, end) => {
  let midpoint  - (start  +  end )  /  2;

  while  (Math.abs(poly(xs, midpoint))  >  0.000001)  {
    if  (poly(xs, midpoint)  * poly(xs, start)  <  0)  {
      end  =  midpoint;
     } else  {
      start  =  midpoint;
     }
    midpoint  =  (start  +  end )  /  2;
   }

  return midpoint;
});



