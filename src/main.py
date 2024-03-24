"""
Main Class: Start program
"""
import arguments
import uuid_custom


if __name__ == '__main__':
    # single uuid
    uuid_value = arguments.get_uuid()
    if uuid_value is not None:
        uuid_custom.check_single_uuid(uuid_value)

    # list of uuids
    uuid_list = arguments.get_list_of_uuids()
    if uuid_list is not None:
        for uuid_value_from_list in uuid_list:
            uuid_custom.check_single_uuid(uuid_value_from_list)
            print("-------------------")

