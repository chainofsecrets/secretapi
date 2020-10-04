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


class InlineResponse2002(object):
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
        'block_height': 'str',
        'validators': 'list[TendermintValidator]'
    }

    attribute_map = {
        'block_height': 'block_height',
        'validators': 'validators'
    }

    def __init__(self, block_height=None, validators=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger"""  # noqa: E501

        self._block_height = None
        self._validators = None
        self.discriminator = None

        if block_height is not None:
            self.block_height = block_height
        if validators is not None:
            self.validators = validators

    @property
    def block_height(self):
        """Gets the block_height of this InlineResponse2002.  # noqa: E501


        :return: The block_height of this InlineResponse2002.  # noqa: E501
        :rtype: str
        """
        return self._block_height

    @block_height.setter
    def block_height(self, block_height):
        """Sets the block_height of this InlineResponse2002.


        :param block_height: The block_height of this InlineResponse2002.  # noqa: E501
        :type: str
        """

        self._block_height = block_height

    @property
    def validators(self):
        """Gets the validators of this InlineResponse2002.  # noqa: E501


        :return: The validators of this InlineResponse2002.  # noqa: E501
        :rtype: list[TendermintValidator]
        """
        return self._validators

    @validators.setter
    def validators(self, validators):
        """Sets the validators of this InlineResponse2002.


        :param validators: The validators of this InlineResponse2002.  # noqa: E501
        :type: list[TendermintValidator]
        """

        self._validators = validators

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
        if issubclass(InlineResponse2002, dict):
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
        if not isinstance(other, InlineResponse2002):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other