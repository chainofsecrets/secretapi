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


class ConsensusState(object):
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
        'chain_id': 'str',
        'height': 'int',
        'root': 'Root',
        'next_validator_set': 'ValidatorSet'
    }

    attribute_map = {
        'chain_id': 'chain_id',
        'height': 'height',
        'root': 'root',
        'next_validator_set': 'next_validator_set'
    }

    def __init__(self, chain_id=None, height=None, root=None, next_validator_set=None):  # noqa: E501
        """ConsensusState - a model defined in Swagger"""  # noqa: E501

        self._chain_id = None
        self._height = None
        self._root = None
        self._next_validator_set = None
        self.discriminator = None

        if chain_id is not None:
            self.chain_id = chain_id
        if height is not None:
            self.height = height
        if root is not None:
            self.root = root
        if next_validator_set is not None:
            self.next_validator_set = next_validator_set

    @property
    def chain_id(self):
        """Gets the chain_id of this ConsensusState.  # noqa: E501


        :return: The chain_id of this ConsensusState.  # noqa: E501
        :rtype: str
        """
        return self._chain_id

    @chain_id.setter
    def chain_id(self, chain_id):
        """Sets the chain_id of this ConsensusState.


        :param chain_id: The chain_id of this ConsensusState.  # noqa: E501
        :type: str
        """

        self._chain_id = chain_id

    @property
    def height(self):
        """Gets the height of this ConsensusState.  # noqa: E501


        :return: The height of this ConsensusState.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ConsensusState.


        :param height: The height of this ConsensusState.  # noqa: E501
        :type: int
        """

        self._height = height

    @property
    def root(self):
        """Gets the root of this ConsensusState.  # noqa: E501


        :return: The root of this ConsensusState.  # noqa: E501
        :rtype: Root
        """
        return self._root

    @root.setter
    def root(self, root):
        """Sets the root of this ConsensusState.


        :param root: The root of this ConsensusState.  # noqa: E501
        :type: Root
        """

        self._root = root

    @property
    def next_validator_set(self):
        """Gets the next_validator_set of this ConsensusState.  # noqa: E501


        :return: The next_validator_set of this ConsensusState.  # noqa: E501
        :rtype: ValidatorSet
        """
        return self._next_validator_set

    @next_validator_set.setter
    def next_validator_set(self, next_validator_set):
        """Sets the next_validator_set of this ConsensusState.


        :param next_validator_set: The next_validator_set of this ConsensusState.  # noqa: E501
        :type: ValidatorSet
        """

        self._next_validator_set = next_validator_set

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
        if issubclass(ConsensusState, dict):
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
        if not isinstance(other, ConsensusState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
