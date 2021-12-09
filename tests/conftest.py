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
from collections import namedtuple

import pytest

from smartpassgen.generators import (
    PassGen, 
    KeyGen,
    gen_base_pass,
    gen_norm_pass,
    gen_smart_pass,
    make_public_key,
    check_public_key,
)


@pytest.fixture(name='context')
def context():
    keys = (
        'login',
        'secret',
        'length',
        'key',
        'norm_pass',
        'smart_pass',
        'seed',
    )
    Info = namedtuple('Info', keys)
    login = 'login'
    secret = 'secret'
    length = 15
    key = '15795be051670afec910bc980189a6011f9f184dea4bbbe4e005e4ca89f3' \
          '18bea963b1a362167b4de909a4f57e1895298f79346068487881c8c969dce4fe909f'
    norm_pass = 'urJ77!IK[9?f6|D'
    smart_pass = 'fRIe?Ro9rE6a6fB'
    seed = '0558e28629b95bfae1e6acd42bcc54882f67f573be685cc0b44279ffa1b9b2d1c2d945fcac' \
           '9f4aadb3bd155a60b486a4f2956ef754372f2025f79c2f7c6eac3b'
    kwargs = dict(
        login=login,
        secret=secret,
        length=length,
        key=key,
        norm_pass=norm_pass,
        smart_pass=smart_pass,
        seed=seed,
    )
    return Info(**kwargs)


@pytest.fixture(name='key_gen')
def obj_key_gen():
    return KeyGen()


@pytest.fixture(name='pass_gen')
def obj_pass_gen():
    return PassGen()


@pytest.fixture(name='func_get_base')
def func_get_base():
    return gen_base_pass


@pytest.fixture(name='func_get_norm')
def func_get_norm():
    return gen_norm_pass


@pytest.fixture(name='func_get_smart')
def func_get_smart():
    return gen_smart_pass


@pytest.fixture(name='func_make_key')
def func_make_key():
    return make_public_key


@pytest.fixture(name='func_check_key')
def func_check_key():
    return check_public_key
