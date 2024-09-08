  const latin_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const extensions = ['txt', 'exe', 'dll'];
  const regex = new RegExp(`^${latin_letters}[${latin_letters}+${latin_letters}.*${extensions.join('|')}$`);
  return regex.test(file_name);
}



