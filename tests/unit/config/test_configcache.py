# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2018 Jay Kamat <jaygkamat@gmail.com>:
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

"""Tests for qutebrowser.misc.autoupdate."""

import pytest

from qutebrowser.config import config


class TestConfigCache:

    @pytest.fixture
    def ccache(self, config_stub):
        return config.configcache

    def test_configcache_except_pattern(self, ccache):
        with pytest.raises(AssertionError):
            assert ccache['content.javascript.enabled']

    def test_configcache_error_set(self, ccache):
        with pytest.raises(TypeError):
            ccache['content.javascript.enabled'] = True

    def test_configcache_get(self, ccache):
        assert not ccache['auto_save.session']
        assert not ccache['auto_save.session']

    def test_configcache_get_after_set(self, ccache):
        assert not ccache['auto_save.session']
        config.val.auto_save.session = True
        assert ccache['auto_save.session']
