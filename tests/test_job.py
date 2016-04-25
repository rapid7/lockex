import pytest
from mock import call
from testfixtures.popen import MockPopen
from testfixtures import Replacer, ShouldRaise, compare

import lockex.execute as execute


def test_job():
    Popen = MockPopen()
    Popen.set_command('top', stdout=b'o', stderr=b'e', returncode=1, pid=1000)
    process = Popen('top', stdout=b'o', stderr=b'e', shell=True)
    process.wait()
    execute.kill_job(process)
    assert process.returncode == 1
