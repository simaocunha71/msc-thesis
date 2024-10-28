  switch (current_planet) {
    case 'Mercury':
      return 'Venus';
    case 'Venus':
      return 'Earth';
    case 'Earth':
      return 'Mars';
    case 'Mars':
      return 'Jupiter';
    case 'Jupiter':
      return 'Saturn';
    case 'Saturn':
      return 'Uranus';
    case 'Uranus':
      return 'Neptune';
    default:
      return 'Mercury';
  }
}



