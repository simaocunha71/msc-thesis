  if (arr.length === 0) return null;
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) sum += -arr[i];
    else if (arr[i] > 0) sum += arr[i];
    else sum += 0;
  }
  return sum * Math.abs(arr.reduce((acc, curr) => acc * curr, 1));
};

/* Alternative solution */
// const prodSigns = (arr) => {
//   const sign = [1, -1, 0];
//   let sum = 0;

//   for (let i = 0; i < arr.length; i++) {
//     sum += sign[arr[i]] * Math.abs(arr[i]);
//   }

//   return sum * Math.abs(arr.reduce((acc, curr) => acc * curr, 1));
// };


/* Alternative solution */
// const prodSigns = (arr) => {
//   let sum = 0;

//   for (let i = 0; i < arr.length; i++) {
//     sum += Math.abs(arr[i]) * (arr[i] > 0 ? 1 : -1);
//   }

//   return sum * Math.abs(arr.reduce((acc, curr) => acc * curr, 1));
// };































/* Alternative solution */
// const prodSigns = (arr) => {
//   const sign = [1, -1, 0];
//   let sum = 0;

//   for (let i = 0; i < arr.length; i++) {
//     sum += sign[arr[i]] * Math.abs(arr[i]);
//   }

//   return sum * Math.abs(arr.reduce((acc, curr) => acc * curr, 1));
// };


/* Alternative solution */
// const prodSigns = (arr