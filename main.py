# # dz k 22 05 2022
# SELECT town_to, TIMEDIFF(time_in, time_out) AS flight_time
# FROM Trip
# WHERE town_from = "Paris"


# SELECT town_to, TIMEDIFF(time_in, time_out) AS flight_time
# FROM Trip
# WHERE town_from = 'Paris'

# 9

# SELECT DISTINCT name
# FROM Company
# JOIN Trip
# on Company.id=Trip.company
# where town_from='Vladivostok'

# 10

# SELECT *
# FROM Trip
# where time_out BETWEEN "1900-01-01T10:30:00.000Z" AND "1900-01-01T14:00:00.000Z"

# 11

# SELECT name
# FROM Passenger
# ORDER BY LENGTH(name) DESC LIMIT 1

# 12


# SELECT trip, COUNT(Passenger) as count
# FROM Pass_in_Trip
# GROUP BY Trip

# 13

# SELECT name
# FROM Passenger
# GROUP BY name
# HAVING COUNT(name) > 1;

# 14

# SELECT town_to
# FROM Trip
# JOIN Passenger
# as
