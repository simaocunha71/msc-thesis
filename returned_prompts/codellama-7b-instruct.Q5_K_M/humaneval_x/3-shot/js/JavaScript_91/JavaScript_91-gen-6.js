  return S.split('.').map((s) => s.split('?').map((s) => s.split('!').length).reduce((a, b) => a + b, 0)).reduce((a, b) => a + b, 0);
}



