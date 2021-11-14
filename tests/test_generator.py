# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


class TestPassGen:
    def test_base_gen(self, pass_gen):
        assert pass_gen.base_gen() != pass_gen.base_gen()

    def test_smart_gen(self, pass_gen, context):
        assert pass_gen.smart_gen(
            login=context.login,
            secret=context.secret,
            length=context.length
        ) == context.smart_pass

    def test_norm_gen(self, pass_gen, context):
        assert pass_gen.norm_gen(
            secret=context.secret,
            length=context.length
        ) == context.norm_pass

    def test__generate(self, pass_gen):
        assert pass_gen._generate() != pass_gen._generate() and (
                pass_gen._generate(seed='test') == pass_gen._generate(seed='test')
        )

    def test__get_seed(self, pass_gen, context):
        assert pass_gen._get_seed(login=context.login, secret=context.secret) == context.seed
