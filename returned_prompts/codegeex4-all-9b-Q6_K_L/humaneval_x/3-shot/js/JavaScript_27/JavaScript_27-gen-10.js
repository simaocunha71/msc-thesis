  return string.split('').map(x => x.toUpperCase() === x ? x.toLowerCase() : x.toUpperCase()).join('');
}