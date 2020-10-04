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


class BlockID(object):
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
        'hash': 'Hash',
        'parts': 'BlockIDParts'
    }

    attribute_map = {
        'hash': 'hash',
        'parts': 'parts'
    }

    def __init__(self, hash=None, parts=None):  # noqa: E501
        """BlockID - a model defined in Swagger"""  # noqa: E501

        self._hash = None
        self._parts = None
        self.discriminator = None

        if hash is not None:
            self.hash = hash
        if parts is not None:
            self.parts = parts

    @property
    def hash(self):
        """Gets the hash of this BlockID.  # noqa: E501


        :return: The hash of this BlockID.  # noqa: E501
        :rtype: Hash
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this BlockID.


        :param hash: The hash of this BlockID.  # noqa: E501
        :type: Hash
        """

        self._hash = hash

    @property
    def parts(self):
        """Gets the parts of this BlockID.  # noqa: E501


        :return: The parts of this BlockID.  # noqa: E501
        :rtype: BlockIDParts
        """
        return self._parts

    @parts.setter
    def parts(self, parts):
        """Sets the parts of this BlockID.


        :param parts: The parts of this BlockID.  # noqa: E501
        :type: BlockIDParts
        """

        self._parts = parts

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
        if issubclass(BlockID, dict):
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
        if not isinstance(other, BlockID):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
