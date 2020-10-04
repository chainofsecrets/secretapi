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


class BlockQuery(object):
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
        'block_meta': 'BlockQueryBlockMeta',
        'block': 'Block'
    }

    attribute_map = {
        'block_meta': 'block_meta',
        'block': 'block'
    }

    def __init__(self, block_meta=None, block=None):  # noqa: E501
        """BlockQuery - a model defined in Swagger"""  # noqa: E501

        self._block_meta = None
        self._block = None
        self.discriminator = None

        if block_meta is not None:
            self.block_meta = block_meta
        if block is not None:
            self.block = block

    @property
    def block_meta(self):
        """Gets the block_meta of this BlockQuery.  # noqa: E501


        :return: The block_meta of this BlockQuery.  # noqa: E501
        :rtype: BlockQueryBlockMeta
        """
        return self._block_meta

    @block_meta.setter
    def block_meta(self, block_meta):
        """Sets the block_meta of this BlockQuery.


        :param block_meta: The block_meta of this BlockQuery.  # noqa: E501
        :type: BlockQueryBlockMeta
        """

        self._block_meta = block_meta

    @property
    def block(self):
        """Gets the block of this BlockQuery.  # noqa: E501


        :return: The block of this BlockQuery.  # noqa: E501
        :rtype: Block
        """
        return self._block

    @block.setter
    def block(self, block):
        """Sets the block of this BlockQuery.


        :param block: The block of this BlockQuery.  # noqa: E501
        :type: Block
        """

        self._block = block

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
        if issubclass(BlockQuery, dict):
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
        if not isinstance(other, BlockQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other