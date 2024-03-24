"""
Handle arguments from command line
"""
import argparse
from argparse import ArgumentParser


def get_uuid():
    """
    Returns UUID from argument list

    :return: UUID
    """
    return raed_arguments().uuid


def get_list_of_uuids():
    """
    With the argument "--list" the path to a file with a list of uuids is given. Here the file is opened and all
    uuids are returned in a list.

    :return: List of UUIDs
    """
    uuid_list = []
    path_to_list = raed_arguments().list
    if path_to_list is not None:
        f = open(path_to_list)
        for uuid_value in f:
            uuid_list.append(uuid_value.strip())
    return uuid_list


def raed_arguments():
    """
    Used Argument parser. Detailed overview with -h.

    :return: parsed arguments
    """
    parser = ArgumentParser(prog=u'''
 __     __                     __   ______                  __    __  __    __  ______  _______  
/  |   /  |                   /  | /      \                /  |  /  |/  |  /  |/      |/       \ 
$$ |   $$ | ______    ______  $$/ /$$$$$$  |__    __       $$ |  $$ |$$ |  $$ |$$$$$$/ $$$$$$$  |
$$ |   $$ |/      \  /      \ /  |$$ |_ $$//  |  /  |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
$$  \ /$$//$$$$$$  |/$$$$$$  |$$ |$$   |   $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
 $$  /$$/ $$    $$ |$$ |  $$/ $$ |$$$$/    $$ |  $$ |      $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |
  $$ $$/  $$$$$$$$/ $$ |      $$ |$$ |     $$ \__$$ |      $$ \__$$ |$$ \__$$ | _$$ |_ $$ |__$$ |
   $$$/   $$       |$$ |      $$ |$$ |     $$    $$ |      $$    $$/ $$    $$/ / $$   |$$    $$/ 
    $/     $$$$$$$/ $$/       $$/ $$/       $$$$$$$ |       $$$$$$/   $$$$$$/  $$$$$$/ $$$$$$$/  
                                           /  \__$$ |                                            
                                           $$    $$/                                             
                                            $$$$$$/                                              
''',
                            description="The program checks UUIDs and outputs further information. If UUIDs are "
                                        "incorrect, the cause of the error is also indicated.",
                            formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-u", "--uuid", dest="uuid",
                        help="UUID to be checked in format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    parser.add_argument("-l", "--list", dest="list",
                        help="Path to file with several UUIDS to verify, one UUID per line. UUID in format "
                             "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

    return parser.parse_args()
