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

    return parser.parse_args()
