  return lst.map(element => Math.ceil(element)).map(element => element ** 2).reduce((accumulator, currentValue) => accumulator + currentValue);
}



