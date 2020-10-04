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


class ValidatorDescription(object):
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
        'moniker': 'str',
        'identity': 'str',
        'website': 'str',
        'security_contact': 'str',
        'details': 'str'
    }

    attribute_map = {
        'moniker': 'moniker',
        'identity': 'identity',
        'website': 'website',
        'security_contact': 'security_contact',
        'details': 'details'
    }

    def __init__(self, moniker=None, identity=None, website=None, security_contact=None, details=None):  # noqa: E501
        """ValidatorDescription - a model defined in Swagger"""  # noqa: E501

        self._moniker = None
        self._identity = None
        self._website = None
        self._security_contact = None
        self._details = None
        self.discriminator = None

        if moniker is not None:
            self.moniker = moniker
        if identity is not None:
            self.identity = identity
        if website is not None:
            self.website = website
        if security_contact is not None:
            self.security_contact = security_contact
        if details is not None:
            self.details = details

    @property
    def moniker(self):
        """Gets the moniker of this ValidatorDescription.  # noqa: E501


        :return: The moniker of this ValidatorDescription.  # noqa: E501
        :rtype: str
        """
        return self._moniker

    @moniker.setter
    def moniker(self, moniker):
        """Sets the moniker of this ValidatorDescription.


        :param moniker: The moniker of this ValidatorDescription.  # noqa: E501
        :type: str
        """

        self._moniker = moniker

    @property
    def identity(self):
        """Gets the identity of this ValidatorDescription.  # noqa: E501


        :return: The identity of this ValidatorDescription.  # noqa: E501
        :rtype: str
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this ValidatorDescription.


        :param identity: The identity of this ValidatorDescription.  # noqa: E501
        :type: str
        """

        self._identity = identity

    @property
    def website(self):
        """Gets the website of this ValidatorDescription.  # noqa: E501


        :return: The website of this ValidatorDescription.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this ValidatorDescription.


        :param website: The website of this ValidatorDescription.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def security_contact(self):
        """Gets the security_contact of this ValidatorDescription.  # noqa: E501


        :return: The security_contact of this ValidatorDescription.  # noqa: E501
        :rtype: str
        """
        return self._security_contact

    @security_contact.setter
    def security_contact(self, security_contact):
        """Sets the security_contact of this ValidatorDescription.


        :param security_contact: The security_contact of this ValidatorDescription.  # noqa: E501
        :type: str
        """

        self._security_contact = security_contact

    @property
    def details(self):
        """Gets the details of this ValidatorDescription.  # noqa: E501


        :return: The details of this ValidatorDescription.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ValidatorDescription.


        :param details: The details of this ValidatorDescription.  # noqa: E501
        :type: str
        """

        self._details = details

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
        if issubclass(ValidatorDescription, dict):
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
        if not isinstance(other, ValidatorDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
