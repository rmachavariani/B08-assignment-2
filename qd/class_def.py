import numpy as np

class Airport:
    def __init__(self, code, x, y):
        self.x = x
        self.y = y
        self.code = code

    def distance(self, target_airport):
        x_dist = abs(self.x - target_airport.x)
        y_dist = abs(self.y - target_airport.y)

        # Calculate distance
        dist = np.sqrt((x_dist ** 2) + (y_dist ** 2))
        return dist


class Fitness:
    def __init__(self, route):
        self.route = route
        self.distance = 0
        self.time = 0
        self.fitness = 0.0

    def routeDistance(self):
        if self.distance == 0:
            pathDistance = 0
            for i in range(len(self.route)):
                startAirport = self.route[i]
                if i + 1 < len(self.route):
                    targetAirport = self.route[i + 1]
                else:
                    targetAirport = self.route[0]
                pathDistance += startAirport.distance(targetAirport)
            self.distance = pathDistance
        return self.distance

    def routeTime(self):
        # speed in km/h
        av_speed = 50
        if (self.time == 0) & (self.distance != 0):
            self.time = self.distance/av_speed + 44
        else:
            self.time = 0
        return self.time

    def routeFitness(self):
        dist = self.routeDistance()
        time = self.routeTime()
        # check if total time is lower than 5 working days of 12 hours
        if (self.fitness == 0):
            self.fitness = 1 / float(dist)
        return self.fitness