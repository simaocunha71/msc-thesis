const planets = {
    Mercury: { distance: 57900000, order: 1 },
    Venus: { distance: 108200000, order: 2 },
    Earth: { distance: 149600000, order: 3 },
    Mars: { distance: 227939200, order: 4 },
    Jupiter: { distance: 778330000, order: 5 },
    Saturn: { distance: 1426666000, order: 6 },
    Uranus: { distance: 2870972000, order: 7 },
    Neptune: { distance: 4497180000, order: 8 }
};

const bf = (planet1, planet2) => {
    if (!(planet1 in planets) || !(planet2 in planets)) {
        return [];
    }

    const order1 = planets[planet1].order;
    const order2 = planets[planet2].order;
    const result = Object.keys(planets)
        .filter(planet => planets[planet].order >= order1 && planets[planet].order <= order2)
        .sort((a, b) => planets[a].distance - planets[b].distance)
        .map(planet => [planet, planets[planet].distance]);

    return result;
};


