# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# smartlegiondev@gmail.com
# --------------------------------------------------------


class TestPassGen:
    def test_generate(self, pass_gen, context):
        assert pass_gen.generate() != pass_gen.generate()
        assert pass_gen.generate(login=context.login) != pass_gen.generate(login=context.login)
        assert pass_gen.generate(login=context.login, secret=context.secret) == context.smart_pass
        assert pass_gen.generate(secret=context.secret) == context.norm_pass

    def test_make_password(self, pass_gen):
        assert pass_gen.make_password() != pass_gen.make_password()
        assert len(pass_gen.make_password(length=30)) == 30
        assert pass_gen.make_password(seed='new') == pass_gen.make_password(seed='new')


class TestKeyGen:
    def test_make(self, key_gen, context):
        assert key_gen.make(login=context.login, secret=context.secret) == context.key

    def test_check(self, key_gen, context):
        assert key_gen.check(login=context.login, secret=context.secret, key=context.key)

    def test__get_hash(self, key_gen):
        assert key_gen._get_hash('Py') != key_gen._get_hash('Yp')


def test_get_base_password(func_get_base, context):
    assert func_get_base(length=context.length) != func_get_base(length=context.length)


def test_get_norm_password(func_get_norm, context):
    assert func_get_norm(secret=context.secret, length=context.length) == context.norm_pass


def test_get_smart_password(func_get_smart, context):
    assert func_get_smart(login=context.login, secret=context.secret, length=context.length) == context.smart_pass


def test_make_public_key(func_make_key, context):
    assert func_make_key(login=context.login, secret=context.secret) == context.key


def test_check_public_key(func_check_key, context):
    assert func_check_key(login=context.login, secret=context.secret, key=context.key)
