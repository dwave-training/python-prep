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

# TODO:  Add code here to define a list containing the names of the
# months. Please use three-character month names, like "Jan" for January.
# Please call it "Months".

# TODO: Add code here to define a dictionary containing the days of the
# month for your current year. Please use three-character month names, like
# "Jan" for "January". Please call it "Days".

num_30 = 0
for Month in Months:
    if Days[Month] == 30:
        num_30 += 1
print(num_30)
