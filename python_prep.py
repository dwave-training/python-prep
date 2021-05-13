# Copyright 2021 D-Wave Systems Inc.
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

def exercise_1(S):

    # TODO: Add up the numbers in S using a for-loop and return the sum.

    return 

def exercise_2(S):

    # TODO: Add up the numbers in S in 2 lines or less and return the sum.

    return 

def exercise_3():

    # TODO: Build a dictionary with:
    #  - keys: tuple of points (x, y)
    #  - values: value of function f = 8x + 3y

    return 

# ------- Main program -------
if __name__ == "__main__":

    S = [1, 2, 3, 4, 5]

    print("\nExercise 1:")
    ex_sum = exercise_1(S)
    print("\tSum:", ex_sum)

    print("\nExercise 2:")
    ex_sum = exercise_2(S)
    print("\tSum:", ex_sum)

    print("\nExercise 3:")
    f = exercise_3()
    for key, val in f.items():
        print("\tInput:", key, "Output:", val)
