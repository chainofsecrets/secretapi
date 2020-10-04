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


class Commit(object):
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
        'block_id': 'BlockID',
        'precommits': 'list[BlockLastCommitPrecommits]'
    }

    attribute_map = {
        'block_id': 'block_id',
        'precommits': 'precommits'
    }

    def __init__(self, block_id=None, precommits=None):  # noqa: E501
        """Commit - a model defined in Swagger"""  # noqa: E501

        self._block_id = None
        self._precommits = None
        self.discriminator = None

        if block_id is not None:
            self.block_id = block_id
        if precommits is not None:
            self.precommits = precommits

    @property
    def block_id(self):
        """Gets the block_id of this Commit.  # noqa: E501


        :return: The block_id of this Commit.  # noqa: E501
        :rtype: BlockID
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this Commit.


        :param block_id: The block_id of this Commit.  # noqa: E501
        :type: BlockID
        """

        self._block_id = block_id

    @property
    def precommits(self):
        """Gets the precommits of this Commit.  # noqa: E501


        :return: The precommits of this Commit.  # noqa: E501
        :rtype: list[BlockLastCommitPrecommits]
        """
        return self._precommits

    @precommits.setter
    def precommits(self, precommits):
        """Sets the precommits of this Commit.


        :param precommits: The precommits of this Commit.  # noqa: E501
        :type: list[BlockLastCommitPrecommits]
        """

        self._precommits = precommits

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
        if issubclass(Commit, dict):
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
        if not isinstance(other, Commit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
