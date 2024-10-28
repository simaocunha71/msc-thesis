  /*const fileNameCheck = file_name => {
    const isValid = file_name.match(/\d{3,}/) ? false : true;
    const isDotPresent = file_name.match(/\./g) ? true : false;
    const isSubstringBeforeDotValid = file_name.match(/^[a-zA-Z]/);
    const isExtensionValid = file_name.match(/.(txt|exe|dll)$/);

    return isValid && isDotPresent && isSubstringBeforeDotValid && isExtensionValid ? 'Yes' : 'No';
  };*/

  const isValid = file_name.match(/\d{3,}/) ? false : true;
  const isDotPresent = file_name.match(/\./g) ? true : false;
  const isSubstringBeforeDotValid = file_name.match(/^[a-zA-Z]/);
  const isExtensionValid = file_name.match(/.(txt|exe|dll)$/);

  return isValid && isDotPresent && isSubstringBeforeDotValid && isExtensionValid ? 'Yes' : 'No';
};

