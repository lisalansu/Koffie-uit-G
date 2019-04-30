import random
from station import Station
from railroad import Railroad
from traject import Trajectory

def make_random_route(railroad, maxLength):
    railroad = railroad
    maxLength = maxLength
    traject = Trajectory(maxLength)

    keylist = []
    for key, value in railroad.station_dict.items():
        keylist.append(key)
    start_station = random.choice(keylist)
    traject.addVisitedStations(start_station)

    while True:
        next_station = random.choice(railroad.station_dict[start_station].connections)
        next_station_name = next_station[0]
        time = next_station[1]

        if traject.length + time < traject.maxLength:
            traject.addVisitedStations(next_station_name)
            traject.addLength(time)

            for connection in railroad.station_dict[start_station].connections:
                if connection[0] == next_station_name and connection[2] == True:
                    traject.addVisitedCritical(connection[3])
                    break
            start_station = next_station_name
        else:
            break

    return ([traject.visitedStations, traject.length, traject.visitedCritical])
