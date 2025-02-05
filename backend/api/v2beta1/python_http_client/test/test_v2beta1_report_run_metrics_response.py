# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import kfp_server_api
from kfp_server_api.models.v2beta1_report_run_metrics_response import V2beta1ReportRunMetricsResponse  # noqa: E501
from kfp_server_api.rest import ApiException

class TestV2beta1ReportRunMetricsResponse(unittest.TestCase):
    """V2beta1ReportRunMetricsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V2beta1ReportRunMetricsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kfp_server_api.models.v2beta1_report_run_metrics_response.V2beta1ReportRunMetricsResponse()  # noqa: E501
        if include_optional :
            return V2beta1ReportRunMetricsResponse(
                metric_name = '0', 
                metric_node_id = '0', 
                status = 'METRICSTATUS_UNSPECIFIED', 
                message = '0'
            )
        else :
            return V2beta1ReportRunMetricsResponse(
        )

    def testV2beta1ReportRunMetricsResponse(self):
        """Test V2beta1ReportRunMetricsResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
