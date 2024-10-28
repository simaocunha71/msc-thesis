const planets = {
  Mercury: {
    orbitalPeriod: 87.969,
    distanceFromSun: 57.909e6,
  },
  Venus: {
    orbitalPeriod: 224.701,
    distanceFromSun: 108.208e6,
  },
  Earth: {
    orbitalPeriod: 365.256,
    distanceFromSun: 149.6e6,
  },
  Mars: {
    orbitalPeriod: 686.98,
    distanceFromSun: 227.93e6,
  },
  Jupiter: {
    orbitalPeriod: 4332.6,
    distanceFromSun: 778.3e6,
  },
  Saturn: {
    orbitalPeriod: 10759,
    distanceFromSun: 1426.6e6,
  },
  Uranus: {
    orbitalPeriod: 30687,
    distanceFromSun: 2872.5e6,
  },
  Neptune: {
    orbitalPeriod: 60190,
    distanceFromSun: 4497e6,
  },
};

const orderByDistanceFromSun = (a, b) => {
  const diff = a.distanceFromSun - b.distanceFromSun;
  if (diff > 0) {
    return 1;
  }
  if (diff < 0) {
    return -1;
  }
  return 0;
};

const between = (start, end) => (planet) => {
  const { distanceFromSun } = planets[planet];
  if (distanceFromSun < start.distanceFromSun || distanceFromSun > end.distanceFromSun) {
    return false;
  }
  return true;
};

const bf = (planet1, planet2) => {
  if (!planets[planet1] || !plan