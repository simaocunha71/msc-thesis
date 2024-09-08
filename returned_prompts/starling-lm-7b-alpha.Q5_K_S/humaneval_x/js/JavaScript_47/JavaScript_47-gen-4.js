  l.sort((a,b)=>a-b);
  let len = l.length;
  if(len%2 === 0){
    return (l[len/2-1]+l[len/2])/2.0;
  }else{
    return l[Math.floor(len/2)];
  }
}



