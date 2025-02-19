# SPDX-License-Identifier: MIT
# pragma version 0.4.0

number_two: public(uint256)
number: public(uint256)

@external
def set_number(new_number: uint256):
    self.number = new_number

@external
def set_number_two(new_number: uint256):
    self.number_two = new_number

@external
def increment():
    self.number += 2

@external 
def decrement():
    self.number -= 1

@external
def version() -> uint256:
    return 2

# @external
# def balanceOf(address: address) -> uint256:
#     return self.balance

# @external
# def branch_passphrase_public(number: uint256, passphrase: bytes8) -> uint256:
#     self.number *= 2
#     return self.number