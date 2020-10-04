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


class Vote(object):
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
        'voter': 'str',
        'proposal_id': 'str',
        'option': 'str'
    }

    attribute_map = {
        'voter': 'voter',
        'proposal_id': 'proposal_id',
        'option': 'option'
    }

    def __init__(self, voter=None, proposal_id=None, option=None):  # noqa: E501
        """Vote - a model defined in Swagger"""  # noqa: E501

        self._voter = None
        self._proposal_id = None
        self._option = None
        self.discriminator = None

        if voter is not None:
            self.voter = voter
        if proposal_id is not None:
            self.proposal_id = proposal_id
        if option is not None:
            self.option = option

    @property
    def voter(self):
        """Gets the voter of this Vote.  # noqa: E501


        :return: The voter of this Vote.  # noqa: E501
        :rtype: str
        """
        return self._voter

    @voter.setter
    def voter(self, voter):
        """Sets the voter of this Vote.


        :param voter: The voter of this Vote.  # noqa: E501
        :type: str
        """

        self._voter = voter

    @property
    def proposal_id(self):
        """Gets the proposal_id of this Vote.  # noqa: E501


        :return: The proposal_id of this Vote.  # noqa: E501
        :rtype: str
        """
        return self._proposal_id

    @proposal_id.setter
    def proposal_id(self, proposal_id):
        """Sets the proposal_id of this Vote.


        :param proposal_id: The proposal_id of this Vote.  # noqa: E501
        :type: str
        """

        self._proposal_id = proposal_id

    @property
    def option(self):
        """Gets the option of this Vote.  # noqa: E501


        :return: The option of this Vote.  # noqa: E501
        :rtype: str
        """
        return self._option

    @option.setter
    def option(self, option):
        """Sets the option of this Vote.


        :param option: The option of this Vote.  # noqa: E501
        :type: str
        """

        self._option = option

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
        if issubclass(Vote, dict):
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
        if not isinstance(other, Vote):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
