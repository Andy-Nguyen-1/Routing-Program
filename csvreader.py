import csv
from hash_table import HashMap

# open and read packages CSV file
with open('Packages.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')
    # Create an instance of HashMap class
    hash_map = HashMap()

    # Truck's delivery list
    first_delivery = []
    second_delivery = []
    third_delivery = []

    # Insert values from csv file into key/value pairs in the hash table. Space-Time Complexity = O(n)
    for row in read_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'

        value = [id, address_location, address, city, state, zip, delivery, size,
                 note, delivery_start, delivery_status]

        # Determines which truck a package should be located and
        # put these packages into a nested list for quick indexing

        # First truck's first delivery
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'None' in value[8]:
                first_delivery.append(value)


        # Second truck's delivery
        if 'Can only be' in value[8] or 'Delayed in flight' in value[8]:
            second_delivery.append(value)

        # Correct incorrect package details
        if '84104' in value[5] and '10:30' not in value[6]:
            third_delivery.append(value)

        # Check remaining packages
        if value not in first_delivery and value not in second_delivery and value not in third_delivery:
            second_delivery.append(value) if len(second_delivery) < len(third_delivery) else third_delivery.append(
                value)

        # Insert values from CSV into the hash table
        hash_map.insert(id, value)


    # Get packages on the first delivery. Space-Time Complexity = O(1)
    def get_first_delivery():
        return first_delivery

    # Get packages on the second delivery. Space-Time Complexity = O(1)
    def get_second_delivery():
        return second_delivery

    # Get packages on the final delivery. Space-Time Complexity = O(1)
    def get_third_delivery():
        return third_delivery

    # Get full list of packages. Space-Time Complexity = O(1)
    def get_hash_map():
        return hash_map