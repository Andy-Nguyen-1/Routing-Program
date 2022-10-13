import csv
import datetime

# Open and read CSV files
with open('Distances.csv') as csvfile_1:
    distance_csv = list(csv.reader(csvfile_1, delimiter=','))
with open('Addresses.csv') as csvfile_2:
    distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))

    # Get package address data from Addresses.CSV
    # Space-Time Complexity = O(n)
    def get_address():
        return distance_name_csv

    # Calculate the total distance from the Distances.csv row/column values
    # Space-Time Complexity = O(1)
    def get_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)

    # Calculate the current distance from Distances.csv row/column values
    # Space-Time Complexity = O(1)
    def get_current_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return float(distance)

    # Calculate total distance for a given truck
    # Space-Time Complexity = O(n)
    def get_time(distance, truck_list):
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins), seconds=int(secs))
        return total


    # Lists that represent the sorted trucks
    first_truck = []
    first_truck_indices = []

    second_truck = []
    second_truck_indices = []

    third_truck = []
    third_truck_indices = []


    # Utilizing the greedy algorithm to find the shortest route. (Section A)
    #
    # In the first for loop it will find the shortest route to the next location.
    # The lowest value will keep updating until it finds a lower value.
    #
    # The second for loop will decide what will happen when it finds a lower value. The closest_location will be added
    # to the sorted truck list and indices list and will also be removed from the unsorted list. This will repeat until
    # base case condition is satisfied which is when the length of the list is zero.
    # Space-Time Complexity = O(n^2)

    def shortest_route(truck_list, truck_num, curr_location):
        #Base case
        if not len(truck_list):
            return truck_list
        # If truck list not empty, set lowest_value and location to 0
        lowest_value = 50.0
        location = 0

        # Get_current_distance of curr_location and next index in truck_list
        for i in truck_list:
            value = int(i[1])
            # If get_current_distance is less than lowest_value
            if get_current_distance(curr_location, value) <= lowest_value:
                # Update new lowest_value as get_current_distance
                lowest_value = get_current_distance(
                    curr_location, value)
                location = value
        # Second for loop
        for i in truck_list:
            # get_current_distance of curr_location and the index in truck_list is equal to lowest_value
            if get_current_distance(curr_location, int(i[1])) == lowest_value:
                if truck_num == 1:
                    first_truck.append(i)
                    first_truck_indices.append(i[1])
                    truck_list.pop(truck_list.index(i))
                    curr_location = location
                    shortest_route(truck_list, 1, curr_location)
                elif truck_num == 2:
                    second_truck.append(i)
                    second_truck_indices.append(i[1])
                    truck_list.pop(truck_list.index(i))
                    curr_location = location
                    shortest_route(truck_list, 2, curr_location)
                elif truck_num == 3:
                    third_truck.append(i)
                    third_truck_indices.append(i[1])
                    truck_list.pop(truck_list.index(i))
                    curr_location = location
                    shortest_route(truck_list, 3, curr_location)

    # Insert 0 for the first index of each index list
    first_truck_indices.insert(0, '0')
    second_truck_indices.insert(0, '0')
    third_truck_indices.insert(0, '0')


    # Returns truck_list and truck_indices_list.
    # Space-Time Complexity = O(1)
    def first_truck_index():
        return first_truck_indices

    def first_truck_list():
        return first_truck

    def second_truck_index():
        return second_truck_indices

    def second_truck_list():
        return second_truck

    def third_truck_index():
        return third_truck_indices

    def third_truck_list():
        return third_truck



