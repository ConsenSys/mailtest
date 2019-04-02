# MailTest
MailTest is a Python unittesting library that for code that sends email.  It starts a local SMTP server inside a Python `with` block, and captures all the email sent to it.  These emails can then be read within the block.

Example:

```
with mailtest.Server() as mt:
    send_welcome_email()
    assert len(mt.emails) == 1
```

## Configuration
Configuration is done via kwargs to `mailtest.Server()`.  Options:
- `smtp_port` (default: 1025)
- `sendgrid_port` (default: `None`)


## Testing
```
$ python2 test.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.269s

OK
```
```
$ python3 test.py 
..
----------------------------------------------------------------------
Ran 2 tests in 0.543s

OK
```

## I am a fork!
Major kudos to the original author, keredson.

https://github.com/keredson/mailtest

The biggest logical difference between the two versions is moving from `bottle` to `flask`.
