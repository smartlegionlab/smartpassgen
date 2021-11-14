# -*- coding: utf-8 -*-
# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2018-2021, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
"""Password generators"""
import os
import random
import string

from smartpassgen.keygen import KeyGen


class PassGen:
    """Password generator"""

    def __init__(self):
        self.symbols = string.ascii_letters + string.digits + '`!@#$%^&()_[]{}"|<>?'
        self.step = 2
        self._key_gen = KeyGen()
        self._key_gen.step = self.step

    def base_gen(self, length=15, size=32):
        """
        Generate base password.

        - A new password will be generated on each call.

        :param length: <int> password length.
        :param size: <int> the number of bytes for the generator.
        :return: <str> base password.
        """
        seed = str(os.urandom(size))
        return self._generate(seed=seed, length=length)

    def smart_gen(self, login='', secret='', length=15):
        """
        Generate smart password.

        - When using the same login and secret
         passphrases will always be the same.

        :param login: <str> - login or any word or phrase.
        :param secret: <str> - any word or phrase.
        :param length: <int> - password length.
        :return: <str> smart password.
        """
        seed = self._get_seed(login=login, secret=secret)
        return self._generate(seed=seed, length=length)

    def norm_gen(self, secret='', length=15):
        """
        Generate smart password.

        - When using the same passphrase, the passwords will always be the same

        :param secret: <str> - any word or phrase.
        :param length: <int> - password length.
        :return: <str> norm smart password.
        """
        return self.smart_gen(login=secret, secret=secret, length=length)

    def _generate(self, seed='', length=15, size=32):
        """
        Generates a password of the specified length using the specified and random seed.

        :param seed: <str> - seed for random.seed
        :param length: <int> - password length.
        :param size: <int> the number of bytes for the generator.
        :return: <str> password
        """
        seed = os.urandom(size) if not seed else seed
        random.seed(seed)
        password = ''.join([random.choice(self.symbols) for _ in range(length)])
        seed = os.urandom(32)
        random.seed(seed)
        return password

    def _get_seed(self, login='', secret=''):
        """
        Generates a seed by generating a public key in step.

        :param login: <str> - login or any word or phrase.
        :param secret: <str> - any word or phrase.
        :return: <str> - key for seed.
        """
        return self._key_gen.make(login=login, secret=secret)
