#!/usr/bin/env python3
"""
tests_task2.py — Unit tests for Task 2: Compression Function

Tests for the compress function in a3_alrod7901.py
"""

import unittest
from a3_alrod7901 import compress, IV, u32


class TestTask2(unittest.TestCase):

    def test_compress_basic(self):
        """Test compress function with IV and zero block."""
        state = IV
        block = b'\x00' * 64
        result = compress(state, block)
        
        # Should return a list of 8 integers
        self.assertEqual(len(result), 8)
        self.assertIsInstance(result, list)
        for w in result:
            self.assertIsInstance(w, int)
            self.assertEqual(w, u32(w))  # Should be u32

    def test_compress_determinism(self):
        """Test that compress is deterministic."""
        state = IV
        block = b'\x00' * 64
        result1 = compress(state, block)
        result2 = compress(state, block)
        self.assertEqual(result1, result2)

    def test_compress_different_state(self):
        """Test that different state gives different output."""
        state1 = IV
        state2 = [u32(x + 1) for x in IV]
        block = b'\x00' * 64
        result1 = compress(state1, block)
        result2 = compress(state2, block)
        self.assertNotEqual(result1, result2)

    def test_compress_different_block(self):
        """Test that different block gives different output."""
        state = IV
        block1 = b'\x00' * 64
        block2 = b'\x01' + b'\x00' * 63
        result1 = compress(state, block1)
        result2 = compress(state, block2)
        self.assertNotEqual(result1, result2)

    def test_compress_invalid_block_length(self):
        """Test that compress raises error for invalid block length."""
        state = IV
        block = b'\x00' * 63  # Not 64 bytes
        with self.assertRaises(ValueError):
            compress(state, block)

    def test_compress_state_length(self):
        """Test that compress works with state of length 8."""
        state = IV  # 8 elements
        block = b'\x00' * 64
        result = compress(state, block)
        self.assertEqual(len(result), 8)


if __name__ == '__main__':
    unittest.main()