# Andy Nguyen
#Student ID 001095861
from csvreader import get_hash_map
from packages import total_distance
import datetime


class Main:
    # This is the user interface for the program
    print('------------------------------------------------------')
    print('Welcome to the WGUPS Routing and Distribution Program!')
    print(f'All packages were delivered and completed in {total_distance():.2f} miles.\n')

    user_input = input("""
    Please use commands below or type 'exit' to quit the program:
    Type 'time' to track all packages from specific time.
    Type 'id' to track package and time with package id.
""")
    # When user input is not exit
    while user_input != 'exit':
        # Case if user types 'time'
        # Get info for all packages at a particular time.
        # Space-Time Complexity = O(n)
        if user_input == 'time':
            try:
                input_time = input('Enter a time in 24 HR format (HH:MM:SS): ')
                (hrs, mins, secs) = input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Space-Time Complexity = O(n^2)
                for count in range(1, 41):
                    try:
                        start_time = get_hash_map().search(str(count))[9]
                        delivery_time = get_hash_map().search(str(count))[10]
                        (hrs, mins, secs) = start_time.split(':')
                        convert_start_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = delivery_time.split(':')
                        convert_delivery_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass

                    # Determines which packages have left the hub by checking all packages against the input time
                    if convert_start_time >= convert_user_time:
                        get_hash_map().search(str(count))[10] = 'At Hub'
                        get_hash_map().search(str(count))[9] = 'Departs at ' + start_time
                        print(
                            f'Package ID: {get_hash_map().search(str(count))[0]}; '
                            f'Delivery Deadline: {get_hash_map().search(str(count))[6]}\n'
                            f'Delivery status: {get_hash_map().search(str(count))[10]}')
                    elif convert_start_time <= convert_user_time:
                        # Determines which packages have left but have not been delivered
                        if convert_user_time < convert_delivery_time:
                            get_hash_map().search(str(count))[10] = 'In transit to destination'
                            get_hash_map().search(str(count))[9] = 'Departed at ' + start_time
                            print(
                                f'Package ID: {get_hash_map().search(str(count))[0]}; '
                                f'Delivery Deadline: {get_hash_map().search(str(count))[6]}\n'
                                f'Delivery status: {get_hash_map().search(str(count))[10]}')
                        # Determines which packages have already been delivered
                        else:
                            get_hash_map().search(str(count))[10] = 'Delivered at ' + delivery_time
                            get_hash_map().search(str(count))[9] = 'Departed at ' + start_time
                            print(
                                f'Package ID: {get_hash_map().search(str(count))[0]}; '
                                f'Delivery Deadline: {get_hash_map().search(str(count))[6]}\n'
                                f'Delivery status: {get_hash_map().search(str(count))[10]}')
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Error!')
                exit()

        # Case if user input is 'id'
        # Get info for a single package at a particular time -> O(n)
        elif user_input == 'id':
            try:
                count = input('Enter the package ID: ')
                start_time = get_hash_map().search(str(count))[9]
                delivery_time = get_hash_map().search(str(count))[10]
                input_time = input('Enter a time in 24 HR format(HH:MM:SS): ')
                (hrs, mins, secs) = input_time.split(':')
                convert_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = start_time.split(':')
                convert_start_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = delivery_time.split(':')
                convert_delivery_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                # Determines which packages have left the hub by checking all packages against the input time
                if convert_start_time >= convert_user_time:

                    get_hash_map().search(str(count))[10] = 'At Hub'
                    get_hash_map().search(str(count))[9] = 'Departs at ' + start_time
                    print(
                        f'Package ID: {get_hash_map().search(str(count))[0]}\n'
                        f'Street address: {get_hash_map().search(str(count))[2]}\n'
                        f'Delivery Deadline: {get_hash_map().search(str(count))[6]}\n'
                        f'Package weight: {get_hash_map().search(str(count))[7]}\n'
                        f'Truck status: {get_hash_map().search(str(count))[9]}\n'
                        f'Delivery status: {get_hash_map().search(str(count))[10]}\n'
                    )

                # Determines which packages have left but have not been delivered
                elif convert_start_time <= convert_user_time:
                    if convert_user_time < convert_delivery_time:
                        get_hash_map().search(str(count))[10] = 'In transit to destination '
                        get_hash_map().search(str(count))[9] = 'Departed at ' + start_time
                        print(
                            f'Package ID: {get_hash_map().search(str(count))[0]}\n'
                            f'Street address: {get_hash_map().search(str(count))[2]}\n'
                            f'Delivery Deadline: {get_hash_map().search(str(count))[6]}\n'
                            f'Package weight: {get_hash_map().search(str(count))[7]}\n'
                            f'Truck status: {get_hash_map().search(str(count))[9]}\n'
                            f'Delivery status: {get_hash_map().search(str(count))[10]}\n'
                        )
                    # Determine which packages have already been delivered
                    else:
                        get_hash_map().search(str(count))[10] = 'Delivered at ' + delivery_time
                        get_hash_map().search(str(count))[9] = 'Departed at ' + start_time
                        print(
                            f'Package ID: {get_hash_map().search(str(count))[0]}\n'
                            f'Street address: {get_hash_map().search(str(count))[2]}\n'
                            f'Delivery Deadline: {get_hash_map().search(str(count))[6]}\n'
                            f'Package weight: {get_hash_map().search(str(count))[7]}\n'
                            f'Truck status: {get_hash_map().search(str(count))[9]}\n'
                            f'Delivery status: {get_hash_map().search(str(count))[10]}\n'
                        )

            except ValueError:
                print('Error!')
                exit()

        # Case if 'exit'
        # This quits the program
        elif user_input == 'quit':
            exit()

        # Case Error
        # Print 'Error!' and quit the program
        else:
            print('Error!')
            exit()