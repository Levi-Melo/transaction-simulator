import random
import math

class CoordinateGenerator:
    def __init__(self):
        self.user_centers = {}

    def get_coordinates_for_user(self, user_id):
        if user_id not in self.user_centers:
            self._set_new_center(user_id)

        center = self.user_centers[user_id]

        # 80% de chance de gerar uma coordenada perto do centro
        if random.random() < 0.8:
            return self._generate_near_coordinates(center)
        else:
            return self._generate_far_coordinates(center)

    def _set_new_center(self, user_id):
        # Gera um centro aleatório para o usuário
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)
        self.user_centers[user_id] = (lat, lon)

    def _generate_near_coordinates(self, center):
        # Gera coordenadas próximas ao centro
        lat_offset = random.uniform(-0.1, 0.1)
        lon_offset = random.uniform(-0.1, 0.1)
        return (center[0] + lat_offset, center[1] + lon_offset)

    def _generate_far_coordinates(self, center):
        # Gera coordenadas mais distantes do centro
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0.5, 2.0)  # Em graus
        new_lat = center[0] + distance * math.cos(angle)
        new_lon = center[1] + distance * math.sin(angle)
        return self._clamp_coordinates(new_lat, new_lon)

    def _clamp_coordinates(self, lat, lon):
        # Garante que as coordenadas estejam dentro dos limites válidos
        return (max(-90, min(90, lat)), max(-180, min(180, lon)))
