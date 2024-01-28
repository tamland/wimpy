# -*- coding: utf-8 -*-
#
# Copyright (C) 2023- The Tidalapi Developers
# Copyright (C) 2019-2022 morguldir
# Copyright (C) 2014 Thomas Amland
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tidalapi

from .cover import verify_image_cover


def test_mix(session):
    mixes = session.mixes()
    first = next(iter(mixes))
    assert isinstance(first, tidalapi.Mix)


def test_image(session):
    mixes = session.mixes()
    first = next(iter(mixes))
    verify_image_cover(session, first, [320, 640, 1500])
