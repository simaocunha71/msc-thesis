  const regex = new RegExp(`[^${substring}]`);
  return strings.filter(s => s.match(regex));
}



