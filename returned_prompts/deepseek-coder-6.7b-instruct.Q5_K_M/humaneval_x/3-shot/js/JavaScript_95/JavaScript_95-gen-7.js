  if  (Object.keys(dict).length  != 0)  {
    let lower  _case  = true;
    let upper  _case  = true;
    for  (let key  in dict)  {
      if  (key  !=  key.toLowerCase())  {
        lower  _case  =  false;
      }
      if  (key  !=  key.toUpperCase())  {
        upper  _case  =  false;
      }
      if  (!lower  _case  &&  !upper  _case)  {
        return false;
      }
    }
    return true;
  }
  else {
    return false;
  }
}



