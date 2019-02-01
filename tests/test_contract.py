from pytest import raises
from web3.contract import ConciseContract
from eth_tester.exceptions import TransactionFailed
from tests.constants import (
    ZERO_ADDR
)

def test_contract(w3, contract, DAI_token, pad_bytes32):
  assert contract.owner() == w3.eth.defaultAccount
  assert contract.name() == pad_bytes32('Stablecoinswap')
  assert contract.decimals() == 18
  assert contract.totalSupply() == 0
  # check used tokens
  assert contract.tokenIsSupported(DAI_token.address)
  assert not contract.tokenIsSupported(w3.eth.accounts[1])