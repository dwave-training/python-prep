# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# TODO:  Add code here to read the file into a string
def read_file_into_string(filename):
    """Returns a string with the file's contents

    Args:
        filename(string): name of the file to open
    """

    # TODO: Add code to read the file into a string

    return data


# TODO:  Add code here to break the string into a list of numbers
def break_file_data_into_list_of_numbers(string_data):
    """Returns a list with the numbers in the file

    Args:
        string_data(string): list of numbers to be parsed
    """

    # TODO: Add code to split the string

    return number_list


## ------- Main program -------
if __name__ == "__main__":

    ## ------- read file into a string --------

    data = read_file_into_string("Numbers_Assignment_PP.txt")

    ## ------ parse string into list -------
    number_list = break_file_data_into_list_of_numbers(data)

    ## ------ sum the list -------
    # TODO: Add code to sum the list - and save to variable sum_of_numbers

    print(sum_of_numbers)
