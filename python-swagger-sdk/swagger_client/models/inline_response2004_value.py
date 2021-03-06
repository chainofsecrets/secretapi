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


class InlineResponse2004Value(object):
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
        'account_number': 'str',
        'address': 'str',
        'coins': 'list[Coin]',
        'public_key': 'PublicKey',
        'sequence': 'str'
    }

    attribute_map = {
        'account_number': 'account_number',
        'address': 'address',
        'coins': 'coins',
        'public_key': 'public_key',
        'sequence': 'sequence'
    }

    def __init__(self, account_number=None, address=None, coins=None, public_key=None, sequence=None):  # noqa: E501
        """InlineResponse2004Value - a model defined in Swagger"""  # noqa: E501

        self._account_number = None
        self._address = None
        self._coins = None
        self._public_key = None
        self._sequence = None
        self.discriminator = None

        if account_number is not None:
            self.account_number = account_number
        if address is not None:
            self.address = address
        if coins is not None:
            self.coins = coins
        if public_key is not None:
            self.public_key = public_key
        if sequence is not None:
            self.sequence = sequence

    @property
    def account_number(self):
        """Gets the account_number of this InlineResponse2004Value.  # noqa: E501


        :return: The account_number of this InlineResponse2004Value.  # noqa: E501
        :rtype: str
        """
        return self._account_number

    @account_number.setter
    def account_number(self, account_number):
        """Sets the account_number of this InlineResponse2004Value.


        :param account_number: The account_number of this InlineResponse2004Value.  # noqa: E501
        :type: str
        """

        self._account_number = account_number

    @property
    def address(self):
        """Gets the address of this InlineResponse2004Value.  # noqa: E501


        :return: The address of this InlineResponse2004Value.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InlineResponse2004Value.


        :param address: The address of this InlineResponse2004Value.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def coins(self):
        """Gets the coins of this InlineResponse2004Value.  # noqa: E501


        :return: The coins of this InlineResponse2004Value.  # noqa: E501
        :rtype: list[Coin]
        """
        return self._coins

    @coins.setter
    def coins(self, coins):
        """Sets the coins of this InlineResponse2004Value.


        :param coins: The coins of this InlineResponse2004Value.  # noqa: E501
        :type: list[Coin]
        """

        self._coins = coins

    @property
    def public_key(self):
        """Gets the public_key of this InlineResponse2004Value.  # noqa: E501


        :return: The public_key of this InlineResponse2004Value.  # noqa: E501
        :rtype: PublicKey
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this InlineResponse2004Value.


        :param public_key: The public_key of this InlineResponse2004Value.  # noqa: E501
        :type: PublicKey
        """

        self._public_key = public_key

    @property
    def sequence(self):
        """Gets the sequence of this InlineResponse2004Value.  # noqa: E501


        :return: The sequence of this InlineResponse2004Value.  # noqa: E501
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this InlineResponse2004Value.


        :param sequence: The sequence of this InlineResponse2004Value.  # noqa: E501
        :type: str
        """

        self._sequence = sequence

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
        if issubclass(InlineResponse2004Value, dict):
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
        if not isinstance(other, InlineResponse2004Value):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
