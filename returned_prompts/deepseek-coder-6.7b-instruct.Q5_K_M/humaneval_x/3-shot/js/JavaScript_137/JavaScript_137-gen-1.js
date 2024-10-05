  let aa = parseFloat(a.replace(",", "."));
  let bb = parseFloat(b.replace(",", "."));

  if  (aa === bb) 
    return null;
  else 
    return (aa > bb) ? a : b;
}



