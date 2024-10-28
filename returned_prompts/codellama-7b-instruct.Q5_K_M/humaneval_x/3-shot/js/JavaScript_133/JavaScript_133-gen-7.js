  return lst.map(element => Math.ceil(element)).map(element => element ** 2).reduce((accumulator, current_element) => accumulator + current_element);
}



