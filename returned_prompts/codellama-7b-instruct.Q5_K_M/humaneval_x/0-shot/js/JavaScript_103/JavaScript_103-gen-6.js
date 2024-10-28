
function roundedAvg(n, m){

  if (n > m) return -1;

  let avg = (n + m) / 2;

  return (Math.round(avg)).toString(2);

}

B:

function roundedAvg(n, m) {

  if (n > m) return -1;

  let avg = (n + m) / 2;

  return (Math.round(avg)).toString(2);
}