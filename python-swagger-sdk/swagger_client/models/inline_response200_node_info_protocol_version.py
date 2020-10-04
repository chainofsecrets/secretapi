# coding: utf-8

"""
    API for Secret Network by ChainofSecrets.org

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InlineResponse200NodeInfoProtocolVersion(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'p2p': 'str',
        'block': 'str',
        'app': 'str'
    }

    attribute_map = {
        'p2p': 'p2p',
        'block': 'block',
        'app': 'app'
    }

    def __init__(self, p2p=None, block=None, app=None):  # noqa: E501
        """InlineResponse200NodeInfoProtocolVersion - a model defined in Swagger"""  # noqa: E501

        self._p2p = None
        self._block = None
        self._app = None
        self.discriminator = None

        if p2p is not None:
            self.p2p = p2p
        if block is not None:
            self.block = block
        if app is not None:
            self.app = app

    @property
    def p2p(self):
        """Gets the p2p of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501


        :return: The p2p of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501
        :rtype: str
        """
        return self._p2p

    @p2p.setter
    def p2p(self, p2p):
        """Sets the p2p of this InlineResponse200NodeInfoProtocolVersion.


        :param p2p: The p2p of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501
        :type: str
        """

        self._p2p = p2p

    @property
    def block(self):
        """Gets the block of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501


        :return: The block of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501
        :rtype: str
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this InlineResponse200NodeInfoProtocolVersion.


        :param block: The block of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501
        :type: str
        """

        self._block = block

    @property
    def app(self):
        """Gets the app of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501


        :return: The app of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this InlineResponse200NodeInfoProtocolVersion.


        :param app: The app of this InlineResponse200NodeInfoProtocolVersion.  # noqa: E501
        :type: str
        """

        self._app = app

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(InlineResponse200NodeInfoProtocolVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InlineResponse200NodeInfoProtocolVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
