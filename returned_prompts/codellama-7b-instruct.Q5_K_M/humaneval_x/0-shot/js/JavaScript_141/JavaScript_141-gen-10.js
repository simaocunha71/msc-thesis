const fileNameCheck = (file_name) => {
  // your code here
  const isValid = /^[a-zA-Z][a-zA-Z0-9]{0,2}\.(?:txt|exe|dll)$/.test(file_name)
  return isValid ? 'Yes' : 'No'
}
