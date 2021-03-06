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


class Block(object):
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
        'header': 'BlockHeader',
        'txs': 'list[str]',
        'evidence': 'list[str]',
        'last_commit': 'BlockLastCommit'
    }

    attribute_map = {
        'header': 'header',
        'txs': 'txs',
        'evidence': 'evidence',
        'last_commit': 'last_commit'
    }

    def __init__(self, header=None, txs=None, evidence=None, last_commit=None):  # noqa: E501
        """Block - a model defined in Swagger"""  # noqa: E501

        self._header = None
        self._txs = None
        self._evidence = None
        self._last_commit = None
        self.discriminator = None

        if header is not None:
            self.header = header
        if txs is not None:
            self.txs = txs
        if evidence is not None:
            self.evidence = evidence
        if last_commit is not None:
            self.last_commit = last_commit

    @property
    def header(self):
        """Gets the header of this Block.  # noqa: E501


        :return: The header of this Block.  # noqa: E501
        :rtype: BlockHeader
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Block.


        :param header: The header of this Block.  # noqa: E501
        :type: BlockHeader
        """

        self._header = header

    @property
    def txs(self):
        """Gets the txs of this Block.  # noqa: E501


        :return: The txs of this Block.  # noqa: E501
        :rtype: list[str]
        """
        return self._txs

    @txs.setter
    def txs(self, txs):
        """Sets the txs of this Block.


        :param txs: The txs of this Block.  # noqa: E501
        :type: list[str]
        """

        self._txs = txs

    @property
    def evidence(self):
        """Gets the evidence of this Block.  # noqa: E501


        :return: The evidence of this Block.  # noqa: E501
        :rtype: list[str]
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        """Sets the evidence of this Block.


        :param evidence: The evidence of this Block.  # noqa: E501
        :type: list[str]
        """

        self._evidence = evidence

    @property
    def last_commit(self):
        """Gets the last_commit of this Block.  # noqa: E501


        :return: The last_commit of this Block.  # noqa: E501
        :rtype: BlockLastCommit
        """
        return self._last_commit

    @last_commit.setter
    def last_commit(self, last_commit):
        """Sets the last_commit of this Block.


        :param last_commit: The last_commit of this Block.  # noqa: E501
        :type: BlockLastCommit
        """

        self._last_commit = last_commit

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
        if issubclass(Block, dict):
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
        if not isinstance(other, Block):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
