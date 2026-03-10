#!/usr/bin/env python3
"""
tests_task1.py — Unit tests for a3_alrod7901.py

Tests for Task 1 functions.
"""

import unittest
from a3_alrod7901 import u32, rotl32, rotr32, xor_bytes, hamming_distance, flip_one_random_bit


class TestTask1(unittest.TestCase):

    def test_u32(self):
        """Test u32 function: force into unsigned 32-bit range."""
        self.assertEqual(u32(0), 0)
        self.assertEqual(u32(0xFFFFFFFF), 0xFFFFFFFF)
        self.assertEqual(u32(0x100000000), 0)  # Overflow
        self.assertEqual(u32(-1), 0xFFFFFFFF)  # Negative
        self.assertEqual(u32(0x1FFFFFFFF), 0xFFFFFFFF)  # Large number

    def test_rotl32(self):
        """Test rotl32: rotate left 32-bit."""
        self.assertEqual(rotl32(0x12345678, 0), 0x12345678)
        self.assertEqual(rotl32(0x12345678, 4), 0x23456781)
        self.assertEqual(rotl32(0x12345678, 8), 0x34567812)
        self.assertEqual(rotl32(0x80000000, 1), 1)  # MSB to LSB
        self.assertEqual(rotl32(0xFFFFFFFF, 16), 0xFFFFFFFF)

    def test_rotr32(self):
        """Test rotr32: rotate right 32-bit."""
        self.assertEqual(rotr32(0x12345678, 0), 0x12345678)
        self.assertEqual(rotr32(0x12345678, 4), 0x81234567)
        self.assertEqual(rotr32(0x12345678, 8), 0x78123456)
        self.assertEqual(rotr32(1, 1), 0x80000000)  # LSB to MSB
        self.assertEqual(rotr32(0xFFFFFFFF, 16), 0xFFFFFFFF)

    def test_xor_bytes(self):
        """Test xor_bytes: XOR two equal-length byte strings."""
        a = b'\x00\x01\x02'
        b = b'\x00\x01\x02'
        self.assertEqual(xor_bytes(a, b), b'\x00\x00\x00')

        a = b'\xFF\x00\xAA'
        b = b'\x00\xFF\x55'
        self.assertEqual(xor_bytes(a, b), b'\xFF\xFF\xFF')

        # Test with different lengths: zip truncates to shorter
        a = b'\x00\x01'
        b = b'\x00\x01\x02'
        self.assertEqual(xor_bytes(a, b), b'\x00\x00')

    def test_hamming_distance(self):
        """Test hamming_distance: bitwise Hamming distance."""
        self.assertEqual(hamming_distance(b'\x00', b'\x00'), 0)
        self.assertEqual(hamming_distance(b'\x00', b'\x01'), 1)
        self.assertEqual(hamming_distance(b'\x00', b'\xFF'), 8)
        self.assertEqual(hamming_distance(b'\xAA', b'\x55'), 8)  # 10101010 ^ 01010101 = 11111111

    def test_flip_one_random_bit(self):
        """Test flip_one_random_bit: exactly one bit flipped."""
        data = b'\x00\x00\x00'
        flipped = flip_one_random_bit(data)
        # Should have exactly one bit different
        diff = xor_bytes(data, flipped)
        self.assertEqual(sum(bin(b).count('1') for b in diff), 1)
        # And same length
        self.assertEqual(len(flipped), len(data))


if __name__ == '__main__':
    unittest.main()