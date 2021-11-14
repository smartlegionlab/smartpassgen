# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestKeyGen:
    def test_make(self, key_gen, context):
        assert key_gen.make(login=context.login, secret=context.secret) == context.key

    def test_check(self, key_gen, context):
        assert key_gen.check(login=context.login, secret=context.secret, key=context.key)

    def test__get_hash(self, key_gen):
        assert key_gen._get_hash('Py') != key_gen._get_hash('Yp')
