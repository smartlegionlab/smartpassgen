# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------


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
