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


class PaginatedQueryTxs(object):
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
        'total_count': 'float',
        'count': 'float',
        'page_number': 'float',
        'page_total': 'float',
        'limit': 'float',
        'txs': 'list[TxQuery]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'count': 'count',
        'page_number': 'page_number',
        'page_total': 'page_total',
        'limit': 'limit',
        'txs': 'txs'
    }

    def __init__(self, total_count=None, count=None, page_number=None, page_total=None, limit=None, txs=None):  # noqa: E501
        """PaginatedQueryTxs - a model defined in Swagger"""  # noqa: E501

        self._total_count = None
        self._count = None
        self._page_number = None
        self._page_total = None
        self._limit = None
        self._txs = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if count is not None:
            self.count = count
        if page_number is not None:
            self.page_number = page_number
        if page_total is not None:
            self.page_total = page_total
        if limit is not None:
            self.limit = limit
        if txs is not None:
            self.txs = txs

    @property
    def total_count(self):
        """Gets the total_count of this PaginatedQueryTxs.  # noqa: E501


        :return: The total_count of this PaginatedQueryTxs.  # noqa: E501
        :rtype: float
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PaginatedQueryTxs.


        :param total_count: The total_count of this PaginatedQueryTxs.  # noqa: E501
        :type: float
        """

        self._total_count = total_count

    @property
    def count(self):
        """Gets the count of this PaginatedQueryTxs.  # noqa: E501


        :return: The count of this PaginatedQueryTxs.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PaginatedQueryTxs.


        :param count: The count of this PaginatedQueryTxs.  # noqa: E501
        :type: float
        """

        self._count = count

    @property
    def page_number(self):
        """Gets the page_number of this PaginatedQueryTxs.  # noqa: E501


        :return: The page_number of this PaginatedQueryTxs.  # noqa: E501
        :rtype: float
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this PaginatedQueryTxs.


        :param page_number: The page_number of this PaginatedQueryTxs.  # noqa: E501
        :type: float
        """

        self._page_number = page_number

    @property
    def page_total(self):
        """Gets the page_total of this PaginatedQueryTxs.  # noqa: E501


        :return: The page_total of this PaginatedQueryTxs.  # noqa: E501
        :rtype: float
        """
        return self._page_total

    @page_total.setter
    def page_total(self, page_total):
        """Sets the page_total of this PaginatedQueryTxs.


        :param page_total: The page_total of this PaginatedQueryTxs.  # noqa: E501
        :type: float
        """

        self._page_total = page_total

    @property
    def limit(self):
        """Gets the limit of this PaginatedQueryTxs.  # noqa: E501


        :return: The limit of this PaginatedQueryTxs.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PaginatedQueryTxs.


        :param limit: The limit of this PaginatedQueryTxs.  # noqa: E501
        :type: float
        """

        self._limit = limit

    @property
    def txs(self):
        """Gets the txs of this PaginatedQueryTxs.  # noqa: E501


        :return: The txs of this PaginatedQueryTxs.  # noqa: E501
        :rtype: list[TxQuery]
        """
        return self._txs

    @txs.setter
    def txs(self, txs):
        """Sets the txs of this PaginatedQueryTxs.


        :param txs: The txs of this PaginatedQueryTxs.  # noqa: E501
        :type: list[TxQuery]
        """

        self._txs = txs

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
        if issubclass(PaginatedQueryTxs, dict):
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
        if not isinstance(other, PaginatedQueryTxs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
