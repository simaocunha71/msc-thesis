  if  (date  != '') {
    let  [month, day, year]  =  date.split('-');
    if  ((month  == '02'  &&  day  <= '29'  &&  [1, 3, 5, 7, 8, 10, 12].includes(parseInt(month)))  ||  (month  == '04'  &&  day  <= '30'  &&  [4, 6, 9, 11].includes(parseInt(month)))  ||  (month  == '06'  &&  day  <= '30'  &&  parseInt(month)  == 6)  ||  (month  == '09'  &&  day  <= '30'  &&  parseInt(month)  == 9)  ||  (month  == '11'  &&  day  <= '30'  &&  parseInt(month)  == 11)  ||  (month  == '01'  &&  day  <= '31'  &&  parseInt(month)  == 1)  ||  (month  == '03'  &&  day  <= '31'  &&  parseInt(month)  == 3)  ||  (month  == '05'  &&  day  <= '31'  &&  parseInt(month)  == 5)  ||  (month  == '07'  &&  day  <= '31'  &&  parseInt(month)  == 7)  ||  (month  == '08'  &&  day  <= '31'  &&  parseInt(month)  == 8)  ||  (month  == '10'  &&  day  <= '31'  &&  parseInt(month)  == 10)  ||  (month  == '12'  &&  day  <= '31'  &&  parseInt(month)  == 12)) {
      return true;
     }
   }
  return false;
}



