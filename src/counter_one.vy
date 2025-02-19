# SPDX-License-Identifier: MIT
# pragma version 0.4.0

number: public(uint256)
number_two: public(uint256)

@external
def set_number(new_number: uint256):
    self.number = new_number

@external
def increment():
    self.number += 1

@external
def version() -> uint256:
    return 1

@external
def set_number_two(new_number: uint256):
    self.number_two = new_number

# @external
# def balanceOf() -> uint256:
#     return self.balance