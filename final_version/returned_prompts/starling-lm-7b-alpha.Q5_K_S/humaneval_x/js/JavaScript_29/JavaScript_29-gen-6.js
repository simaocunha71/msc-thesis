  const regex = new RegExp(`^${prefix}`);

  return strings.filter((str) => regex.test(str));
}



