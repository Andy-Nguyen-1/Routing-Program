import distance
import csvreader

# Empty lists created
first_truck_delivery = []
second_truck_delivery = []
third_truck_delivery = []
first_truck_distances = []
second_truck_distances = []
third_truck_distances = []

# Earliest time the trucks can leave the hub
first_truck_leave_time = ['8:00:00']
second_truck_leave_time = ['9:10:00']
third_truck_leave_time = ['11:00:00']

# Set the delivery start and leave time for the first truck.
# Space-Time Complexity = O(n)
for index, value in enumerate(csvreader.get_first_delivery()):
    csvreader.get_first_delivery()[index][9] = first_truck_leave_time[0]
    first_truck_delivery.append(csvreader.get_first_delivery()[index])

# Compare the first truck's addresses to full address list.
# Space-Time ComplexityO (n^2)
for index, outer in enumerate(first_truck_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            first_truck_distances.append(outer[0])
            first_truck_delivery[index][1] = inner[0]

# Call the greedy algorithm to sort packages for the first truck
distance.shortest_route(first_truck_delivery, 1, 0)
total_distance_1 = 0

# Calculate total distance of the first truck and distance of each package.
# Space-Time Complexity = O(n)
for index in range(len(distance.first_truck_index())):
    try:
        total_distance_1 = distance.get_distance(int(distance.first_truck_index()[index]),
                                                 int(distance.first_truck_index()[index + 1]), total_distance_1)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.first_truck_index()[index]),
                                                                          int(distance.first_truck_index()[index + 1])),
                                            first_truck_leave_time)
        distance.first_truck_list()[index][10] = (str(deliver_package))
        csvreader.get_hash_map().update(int(distance.first_truck_list()[index][0]), first_truck_delivery)
    except IndexError:
        pass

# Set the delivery start and leave time for the second truck.
# Space-Time Complexity = O(n)
for index, value in enumerate(csvreader.get_second_delivery()):
    csvreader.get_second_delivery()[index][9] = second_truck_leave_time[0]
    second_truck_delivery.append(csvreader.get_second_delivery()[index])


# Compare the second truck's addresses to full address list.
# Space-Time Complexity = (n^2)
for index, outer in enumerate(second_truck_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            second_truck_distances.append(outer[0])
            second_truck_delivery[index][1] = inner[0]

# Call the greedy algorithm to sort packages for the second truck
distance.shortest_route(second_truck_delivery, 2, 0)
total_distance_2 = 0

# Calculate total distance of the second truck and distance of each package.
# Space-Time Complexity = O(n)
for index in range(len(distance.second_truck_index())):
    try:
        total_distance_2 = distance.get_distance(int(distance.second_truck_index()[index]),
                                                 int(distance.second_truck_index()[index + 1]), total_distance_2)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.second_truck_index()[index]),
                                                                          int(distance.second_truck_index()[
                                                                                  index + 1])), second_truck_leave_time)
        distance.second_truck_list()[index][10] = (str(deliver_package))
        csvreader.get_hash_map().update(int(distance.second_truck_list()[index][0]), second_truck_delivery)
    except IndexError:
        pass

# Set the delivery start and leave time for the third truck.
# Space-Time Complexity = O(n)
for index, value in enumerate(csvreader.get_third_delivery()):
    csvreader.get_third_delivery()[index][9] = third_truck_leave_time[0]
    third_truck_delivery.append(csvreader.get_third_delivery()[index])

# Compare the third truck's addresses to full address list.
# Space-Time Complexity = (n^2)
for index, outer in enumerate(third_truck_delivery):
    for inner in distance.get_address():
        if outer[2] == inner[2]:
            third_truck_distances.append(outer[0])
            third_truck_delivery[index][1] = inner[0]

# Call the greedy algorithm to sort packages for the third truck
distance.shortest_route(third_truck_delivery, 3, 0)
total_distance_3 = 0

# Calculate total distance of the second truck and distance of each package.
# Space-Time Complexity = O(n)
for index in range(len(distance.third_truck_index())):
    try:
        total_distance_3 = distance.get_distance(int(distance.third_truck_index()[index]),
                                                 int(distance.third_truck_index()[index + 1]), total_distance_3)

        deliver_package = distance.get_time(distance.get_current_distance(int(distance.third_truck_index()[index]),
                                                                          int(distance.third_truck_index()[index + 1])),
                                            third_truck_leave_time)
        distance.third_truck_list()[index][10] = (str(deliver_package))
        csvreader.get_hash_map().update(int(distance.third_truck_list()[index][0]), third_truck_delivery)
    except IndexError:
        pass


# Get the total distances of all packages.
# Space-Time Complexity = O(1)
def total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3
