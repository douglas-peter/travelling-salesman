import random
from typing import Tuple

import numpy as np

class RandomMap:
    def __init__(self, no_cities, grid_size):
        self._no_cities: int = no_cities
        self._grid_size: int = grid_size
        self._map: list = self._generate_map()

    def _generate_map(self) -> list:
        map: list = []
        for i in range(self._no_cities):
            coords: Tuple[float, float] = (random.random() * self._grid_size, random.random() * self._grid_size)
            map.append(coords)
        return map
