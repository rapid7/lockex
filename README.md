lockex
======

lockex is a tool that attempts to acquire a lock from zookeeper prior
to executing a user supplied command.

If lockex cannot aquire a lock, it will block, wait and retry to acquire
the lock. Alernatively instead of blocking, lockex can exit after a given
timeout or immediately. The lock id is generated automatically based on
user supplied command. We also assume that the user command that is to
be run, is executed in the foreground.

By default if the concurrency is set it 1, lockex will try and get lock,
if the concurrency is greater than 1 then lockex will try to acquire a
lock via a semaphore.

lockex will die if the connection to zookeeper is lost, it will continue
to run if the connection is suspended. lockex will do it's best to
cleanup the child process when this happens.

License
-------

Please see COPYING

Use cases:
----------

* You have a producer/consumer based daemons, you can only run one
producer at a time. *lockex* will let you startup many producers but
only one will run if it has acquired a lock.

* A long running cronjob and you want to guarantee that it runs on only
on one host assuming the jobs all start within a small time window.


Installation:
-------------

    pip install https://github.com/rapid7/lockex


Usage:
------

Running *lockex --help* will give you information about how to use
the application. In general,

    lockex OPTIONS -- your_command your_args

*lockex* will treat anything after the '--' as the command that you want
to run. *lockex* will also look for the ZKHOSTS environment variable
to connect to your zookeeper cluster, the format is a comma seperated
list of 'hostname:port'.


Example - Cold standby processes:
---------------------------------

Assuming redis did not have a master/slave capability and you are using
supervisord to run your processes.

On host1, you have a single redis instance running (assuming the data
is stored in a shared location)

    lockex -- /usr/local/bin/redis-server /etc/redis.conf

On host2, you have an identical configuration (with access to the data
in the shared location), run the same command as on host1

    lockex -- /usr/local/bin/redis-server /etc/redis.conf

If and when host1's instance redis dies, host2 will acquire the lock
from zookeeper and startup redis. In a controlled example send host1's
lockex instance with a SIGTERM and it will kill it's child processes.

Example - Cron jobs:
--------------------

Assuming your clocks across all you hosts are in sync (via NTP) and you
wish to run a cronjob only once across your hosts and you wish to build
in some reliability of the job running.

On all your hosts you can execute a job like this

    lockex -t 1 -- sleep 30 && uptime

What the above recipe will do is, every host will race to acquire a lock,
the first host that aquires the lock will wait for 30 seconds before
executing the subsequent 'uptime' command. All the other hosts will try
to acquire the lock but timeout after 1 second.

The uptime command could be a garabage collection process, nightly system
wide checks or anything that is required.

Note: care should be taken to select a sensible sleep and timeout value.

Requirements:
-------------

* A working installation of zookeeper and python2.7 or higher.
* A durable instance of zookeeper (at least three nodes).
* The hosts are all synchronised with ntp.

Vendored packages:
------------------

* lockex/glog.py - https://github.com/benley/python-glog - Copyright (c) 2015 Benjamin Staffin - under 2 clause BSD license.
