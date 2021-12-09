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
import hashlib
import os
import random
import string


class KeyGen:
    def __init__(self):
        self._hash_gen = hashlib.sha3_512
        self.step = 15

    def make(self, login='', secret=''):
        """
        Creates a public key linked to the login and secret phrase.

        :param login: <str> - login or any word or phrase.
        :param secret: <str> - any word or phrase.
        :return: <str> - public key.
        """
        login_hash = self._get_hash(text=login)
        secret_hash = self._get_hash(text=secret)
        all_hash = self._get_hash(text=login_hash + secret_hash)
        for _ in range(self.step):
            temp_hash = self._get_hash(all_hash)
            all_hash = self._get_hash(all_hash + temp_hash + secret_hash)
        return self._get_hash(all_hash)

    def check(self, login='', secret='', key=''):
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
        return self.make(login=login, secret=secret) == key

    def _get_hash(self, text=''):
        """
        Hashes a string.

        :param text: <str> text.
        :return: <str> - Hash string.
        """
        sha = self._hash_gen(text.encode('utf-8'))
        return sha.hexdigest()


class PassGen:

    def __init__(self):
        self.symbols = string.ascii_letters + string.digits + '`!@#$%^&()_[]{}"|<>?'
        self.step = 2
        self.size = 32
        self._key_gen = KeyGen()
        self._key_gen.step = self.step

    def generate(self, login='', secret='', length=15):
        if login and secret:
            seed = self._key_gen.make(login, secret)
        elif secret and not login:
            seed = self._key_gen.make(secret, secret)
        else:
            seed = ''
        return self.make_password(seed, length)

    def make_password(self, seed='', length=15):
        if not seed:
            seed = str(os.urandom(self.size))
        random.seed(seed)
        password = ''.join([random.choice(self.symbols) for _ in range(length)])
        seed = os.urandom(32)
        random.seed(seed)
        return password


class Generators:
    pass_gen = PassGen()
    key_gen = KeyGen()

def gen_base_pass(length=15):
    """
    Generate base password.

    - A new password will be generated on each call.

    :param length: <int> password length.
    :return: <str> base password.
    """
    generator = PassGen()
    return generator.make_password(length=length)


def gen_norm_pass(secret, length=15):
    """
    Generate normal smart password.

    - When using the same passphrase, the passwords will always be the same

    :param secret: <str> - any word or phrase.
    :param length: <int> - password length.
    :return: <str> norm smart password.
    """
    generator = PassGen()
    return generator.generate(secret=secret, length=length)


def gen_smart_pass(login, secret, length=15):
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
    return generator.generate(login=login, secret=secret, length=length)


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
