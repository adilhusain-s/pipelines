# coding: utf-8

"""
    Kubeflow Pipelines API

    This file contains REST API specification for Kubeflow Pipelines. The file is autogenerated from the swagger definition.

    Contact: kubeflow-pipelines@google.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kfp_server_api.configuration import Configuration


class RpcStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'code': 'int',
        'message': 'str',
        'details': 'list[ProtobufAny]'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, code=None, message=None, details=None, local_vars_configuration=None):  # noqa: E501
        """RpcStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._message = None
        self._details = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details

    @property
    def code(self):
        """Gets the code of this RpcStatus.  # noqa: E501

        The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].  # noqa: E501

        :return: The code of this RpcStatus.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RpcStatus.

        The status code, which should be an enum value of [google.rpc.Code][google.rpc.Code].  # noqa: E501

        :param code: The code of this RpcStatus.  # noqa: E501
        :type code: int
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this RpcStatus.  # noqa: E501

        A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.  # noqa: E501

        :return: The message of this RpcStatus.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this RpcStatus.

        A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the [google.rpc.Status.details][google.rpc.Status.details] field, or localized by the client.  # noqa: E501

        :param message: The message of this RpcStatus.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def details(self):
        """Gets the details of this RpcStatus.  # noqa: E501

        A list of messages that carry the error details.  There is a common set of message types for APIs to use.  # noqa: E501

        :return: The details of this RpcStatus.  # noqa: E501
        :rtype: list[ProtobufAny]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this RpcStatus.

        A list of messages that carry the error details.  There is a common set of message types for APIs to use.  # noqa: E501

        :param details: The details of this RpcStatus.  # noqa: E501
        :type details: list[ProtobufAny]
        """

        self._details = details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RpcStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RpcStatus):
            return True

        return self.to_dict() != other.to_dict()
