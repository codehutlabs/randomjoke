#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `randomjoke` package."""


import unittest
from click.testing import CliRunner

from randomjoke import randomjoke
from randomjoke import cli


class TestRandomjoke(unittest.TestCase):
    """Tests for `randomjoke` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output
