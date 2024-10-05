
const totalMatch = (lst1, lst2) => {
  let total1 = 0;
  let total2 = 0;
  let result;
  for (let i = 0; i < lst1.length; i++) {
    total1 += lst1[i].length;
  }
  for (let i = 0; i < lst2.length; i++) {
    total2 += lst2[i].length;
  }

  if (total1 < total2) {
    result = lst2;
  } else if (total1 > total2) {
    result = lst1;
  } else {
    result = lst1;
  }
  return result;
};


//   let total1 = 0;
//   let total2 = 0;
//   for (let i = 0; i < lst1.length; i++) {
//     total1 += lst1[i].length;
//   }
//   for (let i = 0; i < lst2.length; i++) {
//     total2 += lst2[i].length;
//   }
//   if (total1 > total2) {
//     return lst1;
//   } else {
//     return lst2;
//   }
// };














































































































































































































