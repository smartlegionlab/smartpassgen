# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Tools for generating passwords, creating and verifying public keys."""
from smartpassgen.generator import PassGen
from smartpassgen.keygen import KeyGen


def get_base_password(length=15):
    """
    Generate base password.

    - A new password will be generated on each call.

    :param length: <int> password length.
    :return: <str> base password.
    """
    generator = PassGen()
    return generator.base_gen(length=length)


def get_norm_password(secret='', length=15):
    """
    Generate smart password.

    - When using the same passphrase, the passwords will always be the same

    :param secret: <str> - any word or phrase.
    :param length: <int> - password length.
    :return: <str> norm smart password.
    """
    generator = PassGen()
    return generator.norm_gen(secret=secret, length=length)


def get_smart_password(login='', secret='', length=15):
    """
    Generate smart password.

    - When using the same login and secret
     passphrases will always be the same.

    :param login: <str> - login or any word or phrase.
    :param secret: <str> - any word or phrase.
    :param length: <int> - password length.
    :return: <str> smart password.
    """
    generator = PassGen()
    return generator.smart_gen(login=login, secret=secret, length=length)


def make_public_key(login='', secret=''):
    """
    Creates a public key linked to the login and secret phrase.

    :param login: <str> - login or any word or phrase.
    :param secret: <str> - any word or phrase.
    :return: <str> - public key.
    """
    key_gen = KeyGen()
    return key_gen.make(login=login, secret=secret)


def check_public_key(login='', secret='', key=''):
    """
    Checking the pair login + secret phrase for
    compliance with the public key.

    - If the pair login + secret phrase are the same,
     what were used to generate the public key,
     will return True.

    :param login: <str> - login or any word or phrase.
    :param secret: <str> - any word or phrase.
    :param key: <str> - public key.
    :return: <bool> - logical check status.
    """
    key_gen = KeyGen()
    return key_gen.check(login=login, secret=secret, key=key)


class Generator:
    """Password and keys generator."""
    pass_gen = PassGen()
    key_gen = KeyGen()
