connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
]

total_connections = 0
total_flight_time = 0

for connection in connections:
    city_from, city_to, flight_time = connection
    if city_to == 'Rome':
        total_connections += 1
        total_flight_time += flight_time

average_flight_time = total_flight_time / total_connections

print("{} connections lead to Rome with an average flight time of {} minutes".format(total_connections, average_flight_time))
