import src.uuid_custom as uuid_custom


# get_uuid_variant
def test_get_uuid_variant_rfc():
    uuid_value = "b30eb6bd-c89a-383d-ba4a-0e6764a8385f"
    result = uuid_custom.get_uuid_variant(uuid_value)
    assert result == "specified in RFC 4122"


def test_get_uuid_variant_wrong_uuid():
    uuid_value = "b30eb6bd-c89a-383d-ea4a-0e6764a8385f"
    assert uuid_custom.get_uuid_variant(uuid_value) == "reserved for future definition"


# get_uuid_version
def test_get_uuid_version_4():
    uuid_value = "b30eb6bd-c89a-483d-ba4a-0e6764a8385f"
    result = uuid_custom.get_uuid_version(uuid_value)
    assert result == "4"


def test_get_uuid_version_wrong_uuid():
    uuid_value = "b30eb6bd-c89a-683d-ba4a-0e6764a8385f"
    assert uuid_custom.get_uuid_version(uuid_value) == "Incorrect Version, only Version 1-5 is valid. Version of given UUID: 6"


# validate_uuid_with_pattern
def test_validate_uuid_with_pattern_ok():
    uuid_value = "b30eb6bd-c89a-383d-ba4a-0e6764a8385f"
    assert uuid_custom.is_uuid_valid(uuid_value)


def test_validate_uuid_with_pattern_capital_letter_ok():
    uuid_value = "b30eb6bd-c89a-383D-ba4a-0e6764a8385F"
    assert uuid_custom.is_uuid_valid(uuid_value)


def test_validate_uuid_with_pattern_wrong_pattern():
    uuid_value = "b30eb6bd-c89a-383d-ba4a-0e6f"
    assert not uuid_custom.is_uuid_valid(uuid_value)


# check_why_uuid_is_not_valid
def test_check_why_uuid_is_not_valid_valid_uuid():
    uuid_value = "b30eb6bd-c89a-383d-ba4a-0e6764a8385f"
    assert uuid_custom.check_why_uuid_is_not_valid(uuid_value) == "UUID is valid"


def test_check_why_uuid_is_not_valid_non_hexadecimal_number():
    uuid_value = "b30eb6Zd-c89a-383G-ba4a-0e6764a8385f"
    assert uuid_custom.check_why_uuid_is_not_valid(uuid_value) == "Only hexadecimal numbers are allowed, not case sensitive. 0-9 a-f"


def test_check_why_uuid_is_not_valid_patter_8_4_4_4_12():
    uuid_value = "b3bd-c89a-383d-ba4a-0e6764a8385f"
    assert uuid_custom.check_why_uuid_is_not_valid(uuid_value) == "UUID does not match format 8-4-4-4-12, example xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"


def test_check_why_uuid_is_not_valid_invalid_version():
    uuid_value = "b30eb6bd-c89a-683d-ba4a-0e6764a8385f"
    assert uuid_custom.check_why_uuid_is_not_valid(uuid_value) == "Incorrect Version, only Version 1-5 is valid. Version of given UUID: 6"


def test_check_why_uuid_is_not_valid_invalid_variant():
    uuid_value = "b30eb6bd-c89a-383d-fa4a-0e6764a8385f"
    assert uuid_custom.check_why_uuid_is_not_valid(uuid_value) == "Incorrect variant, reserved for future definition"
