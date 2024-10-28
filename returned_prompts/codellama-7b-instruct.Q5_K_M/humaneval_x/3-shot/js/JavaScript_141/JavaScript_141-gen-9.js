  if (file_name.match(/[0-9]./)) {
    return 'No'
  }

  if (file_name.match(/\./)) {
    if (file_name.match(/\.[a-z]{3}/)) {
      return 'Yes'
    } else {
      return 'No'
    }
  } else {
    return 'No'
  }
}



