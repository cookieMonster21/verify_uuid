"""
Handle UUIDs.
"""
import re
# uuid library implemented according RFC 4122
import uuid


def is_uuid_valid(uuid_value):
    """
    Checks, if UUID is valid.

    Format: 8-4-4-4-12 (xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx), not case-sensitive
    M: version, only 1-5 available
    N: variant, only 0-9a-d available
    """
    uuid_pattern = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-5][0-9a-fA-F]{3}-[0-9a-dA-D][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"
    if re.match(uuid_pattern, uuid_value):
        return True
    else:
        return False


def check_why_uuid_is_not_valid(uuid_value):
    """
    Checks, why UUID is not valid.
    - Check if UUID is valid
    - Check if only hexadecimal numbers are used
    - Check pattern 8-4-4-12
    - Check Version (1-5)
    - Check Variant
    -> Reason not found

    :param uuid_value: UUID
    :return: String as Reason
    """
    if is_uuid_valid(uuid_value):
        return "UUID is valid"
    # none hexadecimal numbers
    if not re.match("^[0-9a-fA-F-]*$", uuid_value):
        return "Only hexadecimal numbers are allowed, not case sensitive. 0-9 a-f"
    # wrong pattern 8-4-4-4-12
    if not re.match("^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$", uuid_value):
        return "UUID does not match format 8-4-4-4-12, example xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    # invalid version
    version = get_uuid_version(uuid_value)
    if not re.match("^[0-5]$", version):
        return version
    # invalid variant
    variant = get_uuid_variant(uuid_value)
    if not re.match("^[0-9a-dA-D]$", variant):
        return "Incorrect variant, " + variant
    return "Reason not found"


def get_uuid_variant(uuid_value):
    """
    Returns UUID Variant.

    :param uuid_value: UUID
    :return: Variant as String
    """
    return uuid.UUID(uuid_value).variant


def get_uuid_version(uuid_value):
    """
    Returns UUID Version

    :param uuid_value: UUID
    :return: Version or reason when version is invalid
    """
    # 15th position of UUID
    version = uuid_value[14]
    if re.match("^[0-5]$", version):
        return version
    else:
        return "Incorrect Version, only Version 1-5 is valid. Version of given UUID: " + version

