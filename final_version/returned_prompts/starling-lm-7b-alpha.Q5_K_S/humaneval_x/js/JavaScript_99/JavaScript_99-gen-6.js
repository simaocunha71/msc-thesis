  let d = Math.abs(+value - Math.floor(+value));
  return d > 0.5 ? Math.floor(+value) + (d < 0.5 ? 1 : 0) : Math.floor(+value) - (d < 0.5 ? 1 : 0);
}



