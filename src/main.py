"""
Main Class: Starting program with following path:
    1. Validate UUID
        if valid: 1a. Print Variant and Version
        if not valid: 1b. Identify Reason why UUID is not valid
"""
import arguments
import uuid_custom


if __name__ == '__main__':
    # uuid
    uuid_value = arguments.get_uuid()

    # check if uuid is valid
    is_valid = uuid_custom.is_uuid_valid(uuid_value)
    print("UUID is " + "valid" if is_valid else "not valid")

    # if uuid is valid get further information else check reason
    if is_valid:
        # variant
        variant = uuid_custom.get_uuid_variant(uuid_value)
        print("Variant of the UUID: " + variant)
        # version
        version = uuid_custom.get_uuid_version(uuid_value)
        print("Version: " + version)
    else:
        print(uuid_custom.check_why_uuid_is_not_valid(uuid_value))