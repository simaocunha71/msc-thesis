  const values = [[1000,'m'],[900,'cm'],[500,'d'],[400,'cd'],
                  [100,'c'],[90,'xc'],[50,'l'],[40,'xl'],
                  [10,'x'],[9,'ix'],[5,'v'],[4,'iv'],
                  [1,'i']];

  let result = '';
  for (let i = 0; i < values.length; i++) {
    while (number >= values[i][0]) {
      result += values[i][1];
      number -= values[i][0];
    }
  }

  return result;
}



