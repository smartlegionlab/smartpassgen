# smartpassgen

***

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartpassgen)](https://github.com/smartlegionlab/smartpassgen/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartpassgen?label=pypi%20downloads)](https://pypi.org/project/smartpassgen/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartpassgen)
[![PyPI](https://img.shields.io/pypi/v/smartpassgen)](https://pypi.org/project/smartpassgen)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartpassgen)](https://github.com/smartlegionlab/smartpassgen/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartpassgen)](https://pypi.org/project/smartpassgen)

***


Author and developer: ___A.A Suvorov___

[![smartlegiondev@gmail.com](https://img.shields.io/static/v1?label=email:&message=smartlegiondev@gmail.com&color=blue)](mailto:smartlegiondev@gmail.com)

***

## Help the project financially:

- Yandex Money: [https://yoomoney.ru/to/4100115206129186](https://yoomoney.ru/to/4100115206129186)
- PayPal: [https://paypal.me/smartlegionlab](https://paypal.me/smartlegionlab)
- LiberaPay: [https://liberapay.com/smartlegion/donate](https://liberapay.com/smartlegion/donate)
- Visa: 4048 0250 0089 5923

***

## Short Description:
___smartpassgen___ - A cross-platform package of modules for generating complex, smart, generated and recoverable passwords "on the fly", linked to a login and a secret phrase. 

***

## Supported:

- Linux: All.
- Windows: 7/8/10.
- Termux (Android).

***

## What's new?:

___smartpassgen v0.3.0___

- Global code refactoring 

#### Warning:

smartpassgen is still under development, so I can't promise
backward compatibility with older versions! 

Each new version will likely change passwords when generated. This is due to the very specifics of generation,
with increasing or decreasing complexity, or fixing and adding new levels of security.
Therefore, until the package is stable, specify for your applications the exact version of the package, which
you used during development .

***

## Description:

___smartpassgen___ - A cross-platform package of modules for generating complex, smart, generated and recoverable passwords "on the fly", linked to a login and a secret phrase.

With this package, you can create complex cryptographic recoverable smart passwords.

You can generate:

- Normal complex passwords without the possibility of recovery.
- Smart passwords linked to a secret word.
- Smart passwords linked to login and secret phrase.

The login can be the actual login of the resource or any word or phrase.
The secret phrase can be any word or phrase of any length.

## About passwords and security:

Password must be:

- Complex, consisting of letters in different registers, numbers and symbols.
- Long enough to be difficult to pick up.

But how do you remember such a password? This is the main problem with passwords.
Users most often create short, simple passwords that are easy to guess.
Moreover, many keep them open.

There are managers who generate complex passwords and store them in encrypted form,
this is better, but also not very secure, especially since you cannot sync them between devices.
Well, either it requires additional actions.

The idea behind smart passwords is this. Passwords are not stored anywhere, they are generated on the fly.
For a pair of login + secret phrase, the password will always be the same. You can use any length of the password.
The characters will be counted from left to right. The desired slice is selected.

Thus, you can be cross-platform generate your password on any device using a pair of login + secret phrase.

What should be the login?

- The login can be a valid resource login - for convenience, or any word or phrase.

What should be the secret phrase?

- The secret phrase can be any word or phrase of any length.

What is the meaning of the secret phrase?

- The secret phrase is much easier to remember and much more difficult to pick up.
“It doesn't need to be stored, recorded or encrypted somewhere.
- The secret phrase is stored in the most secure place - in your head.
- You can use different logins, and the same secret phrase will be different passwords.

But how do you store such passwords, or create a password manager?

You can use the public key for this!

- Get login + secret phrase + password length from the user.
- Generate a public key.
- Generate a password.
- Show the password to the user.
- Save your login + public key.

How to check the entered data for generating a password?

- You get a secret phrase from the user.
- Use login + passphrase + public key to verify the authenticity of the entered data using the check method of the KeyGen object.

This method generates a new key from the login + secret phrase pair, compares it with the existing key, and returns the logical comparison status.
If the status is True:

- Generate a smart password using login + secret phrase + password length.
- Show to the user.

It is impossible to deceive such a system. Even if you change the verification code and always return true,
it will still not be possible to generate the correct password, since only
a secret phrase that only the user knows. Therefore, such a check is as safe as possible.



***

Attention!

Generator steps for generating a password must always be less than a step for generating a public key!

***

## Install and use:

### Install:

- `python3 -m venv venv`
- `source venv/bin/activate`
- `pip3 install smartpassgen`

or:

- download source code
- unpack
- Go to the project folder
- `python3 -m venv venv`
- `source venv/bin/activate`
- `python3 setup.py install`

***

### Use:

```python
from smartpassgen import Generator

login = 'login'
secret = 'secret'
length = 15

generator = Generator()

base_password = generator.pass_gen.base()
base_password2 = generator.pass_gen.base()
assert base_password != base_password2

norm_password = generator.pass_gen.norm(secret=secret, length=length)
norm_password2 = generator.pass_gen.norm(secret=secret, length=length)
assert norm_password == norm_password2

smart_password = generator.pass_gen.smart(login=login, secret=secret)
smart_password2 = generator.pass_gen.smart(login=login, secret=secret)

assert smart_password == smart_password

key = generator.key_gen.make(login, secret)

assert generator.key_gen.check(login, secret, key)

```
### Test:
For run tests:

- `pip3 install pytest`
- `pytest -v`

For run tests coverage:

- `pip3 install pytest-cov`
- `pytest --cov --cov-report=html`

### Test coverage:

Coverage 100% !!!

***

![coverage img](https://github.com/smartlegionlab/smartpassgen/raw/master/data/images/smartpassgen.png)


***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2021, A.A Suvorov
    All rights reserved.
    --------------------------------------------------------
