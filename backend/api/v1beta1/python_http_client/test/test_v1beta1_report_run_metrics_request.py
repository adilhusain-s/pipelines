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
from kfp_server_api.models.v1beta1_report_run_metrics_request import V1beta1ReportRunMetricsRequest  # noqa: E501
from kfp_server_api.rest import ApiException

class TestV1beta1ReportRunMetricsRequest(unittest.TestCase):
    """V1beta1ReportRunMetricsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1beta1ReportRunMetricsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kfp_server_api.models.v1beta1_report_run_metrics_request.V1beta1ReportRunMetricsRequest()  # noqa: E501
        if include_optional :
            return V1beta1ReportRunMetricsRequest(
                run_id = '0', 
                metrics = [
                    kfp_server_api.models.v1beta1_run_metric.v1beta1RunMetric(
                        name = '0', 
                        node_id = '0', 
                        number_value = 1.337, 
                        format = 'UNSPECIFIED', )
                    ]
            )
        else :
            return V1beta1ReportRunMetricsRequest(
        )

    def testV1beta1ReportRunMetricsRequest(self):
        """Test V1beta1ReportRunMetricsRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
