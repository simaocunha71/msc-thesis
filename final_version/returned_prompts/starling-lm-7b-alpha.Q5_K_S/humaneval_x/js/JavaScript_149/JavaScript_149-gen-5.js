  lst.sort(function(a,b){
    if(a.length == b.length){
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
  return lst.filter(function(a){
    return a.length%2 === 0;
  });
}



