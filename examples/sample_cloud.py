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

This is a sample implementation of a cloud module that can be used with Icetea.
It does nothing but provides an example of a module that could be used to store testcase results,
campaigns, suites etc.

@Author: Joonas Nikula
"""
# pylint: disable=unused-argument,too-many-arguments


def create(host, port, result_converter=None, testcase_converter=None, args=None):
    """
    Function which is called by Icetea to create an instance of the cloud client. This function
    must exists.
    This function myust not return None. Either return an instance of Client or raise.
    """
    return SampleClient(host, port, result_converter, testcase_converter, args)


class SampleClient(object):
    """
    Example of a cloud client class.
    """
    def __init__(self, host='localhost', port=3000, result_converter=None,
                 testcase_converter=None, args=None):
        # Optional converter for result data from format provided by test framework to
        # format supported by server
        self.result_converter = result_converter
        # Optional converter for testcase metadata from format provided by test framework to
        # one supported by server
        self.tc_converter = testcase_converter

        self.host = host
        self.port = port

    def set_logger(self, logger):
        '''
        Set Logger
        :param logger:  Logger -oject
        '''
        pass

    def get_suite(self, suite, options):
        '''
        Get suite from server.

        returns suite information as a dictionary object.
        '''
        pass

    def get_campaign_id(self, campaign_name):
        """
        Get ID of campaign that has name campaign_name
        """
        pass

    def get_campaigns(self):
        """
        Get campaigns from server
        """
        pass

    def get_campaign_names(self):
        """
        Get names of campaigns from server

        returns list of campaign/suite names.
        """
        pass

    def update_testcase(self, metadata):
        """
        Update TC data to server or create a new testcase on server.

        If testcase_converter has been provided,
        use it to convert TC metadata to format accepted by the server.
        """
        pass

    def send_results(self, result):
        """
        Upload a result object to server.
        If resultConverter has been provided, use it to convert result object to format accepted
        by the server.
        If needed, use testcase_converter to convert tc metadata in result to suitable format.

        returns new result entry as a dictionary or None.
        """
        if self.result_converter:
            print(self.result_converter(result))
        else:
            print(result)
