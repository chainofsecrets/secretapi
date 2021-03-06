# coding: utf-8

"""
    API for Secret Network by ChainofSecrets.org

    A REST interface for state queries, transaction generation and broadcasting.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.staking_api import StakingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestStakingApi(unittest.TestCase):
    """StakingApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.staking_api.StakingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_staking_delegators_delegator_addr_delegations_get(self):
        """Test case for staking_delegators_delegator_addr_delegations_get

        Get all delegations from a delegator  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_delegations_post(self):
        """Test case for staking_delegators_delegator_addr_delegations_post

        Submit delegation  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_delegations_validator_addr_get(self):
        """Test case for staking_delegators_delegator_addr_delegations_validator_addr_get

        Query the current delegation between a delegator and a validator  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_redelegations_post(self):
        """Test case for staking_delegators_delegator_addr_redelegations_post

        Submit a redelegation  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_unbonding_delegations_get(self):
        """Test case for staking_delegators_delegator_addr_unbonding_delegations_get

        Get all unbonding delegations from a delegator  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_unbonding_delegations_post(self):
        """Test case for staking_delegators_delegator_addr_unbonding_delegations_post

        Submit an unbonding delegation  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get(self):
        """Test case for staking_delegators_delegator_addr_unbonding_delegations_validator_addr_get

        Query all unbonding delegations between a delegator and a validator  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_validators_get(self):
        """Test case for staking_delegators_delegator_addr_validators_get

        Query all validators that a delegator is bonded to  # noqa: E501
        """
        pass

    def test_staking_delegators_delegator_addr_validators_validator_addr_get(self):
        """Test case for staking_delegators_delegator_addr_validators_validator_addr_get

        Query a validator that a delegator is bonded to  # noqa: E501
        """
        pass

    def test_staking_parameters_get(self):
        """Test case for staking_parameters_get

        Get the current staking parameter values  # noqa: E501
        """
        pass

    def test_staking_pool_get(self):
        """Test case for staking_pool_get

        Get the current state of the staking pool  # noqa: E501
        """
        pass

    def test_staking_redelegations_get(self):
        """Test case for staking_redelegations_get

        Get all redelegations (filter by query params)  # noqa: E501
        """
        pass

    def test_staking_validators_get(self):
        """Test case for staking_validators_get

        Get all validator candidates. By default it returns only the bonded validators.  # noqa: E501
        """
        pass

    def test_staking_validators_validator_addr_delegations_get(self):
        """Test case for staking_validators_validator_addr_delegations_get

        Get all delegations from a validator  # noqa: E501
        """
        pass

    def test_staking_validators_validator_addr_get(self):
        """Test case for staking_validators_validator_addr_get

        Query the information from a single validator  # noqa: E501
        """
        pass

    def test_staking_validators_validator_addr_unbonding_delegations_get(self):
        """Test case for staking_validators_validator_addr_unbonding_delegations_get

        Get all unbonding delegations from a validator  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
