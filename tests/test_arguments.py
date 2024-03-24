import argparse
import pytest

import src.arguments as arguments


# get_list_of_uuids
def test_get_list_of_uuids_ok(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args',
                 return_value=argparse.Namespace(list='./files/test_get_list_of_uuids_ok.txt'))
    expected = ["b30eb6bd-c89a-483d-8a4a-0e6764a8385f", "3ff971b1-8b16-4ede-90b0-2d3ac5a9f8d3"]
    result = arguments.get_list_of_uuids()
    assert result == expected


def test_get_list_of_uuids_empty_list(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args',
                 return_value=argparse.Namespace(list='./files/test_get_list_of_uuids_empty_list.txt'))
    expected = []
    result = arguments.get_list_of_uuids()
    assert result == expected


def test_get_list_of_uuids_non_existing_file(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args',
                 return_value=argparse.Namespace(list='./files/non_existing_file.txt'))
    with pytest.raises(FileNotFoundError):
        arguments.get_list_of_uuids()
