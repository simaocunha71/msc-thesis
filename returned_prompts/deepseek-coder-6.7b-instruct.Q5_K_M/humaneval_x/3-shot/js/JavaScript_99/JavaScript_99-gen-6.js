  var float_value = parseFloat(value);
  var int_value 
  if(float_value < 0){
      int_value = Math.floor(float_value);
  }
  else {
      int_value = Math.ceil(float_value);
  }
  return int_value;
}



