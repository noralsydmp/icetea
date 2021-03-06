"""
Copyright 2017 ARM Limited
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from icetea_lib.bench import Bench
from icetea_lib.TestStepError import TestStepFail


class Testcase(Bench):
    """
    This test case should always result in a failure.
    """
    def __init__(self):
        Bench.__init__(self,
                       name="test_run_retcodes_fail",
                       title="unittest dut crash in testcase",
                       status="development",
                       type="acceptance",
                       purpose="dummy",
                       component=["Icetea_ut"],
                       requirements={
                           "duts": {
                               '*': {
                                   "count": 0
                               }
                           }}
                      )

    def case(self):  # pylint: disable=no-self-use
        """
        Raise a TestStepFail to fail the test case.
        """
        raise TestStepFail("This must fail!")
