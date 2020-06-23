#########
BuggyBase
#########

A vulnerable app to use in my school class "BugHunt 101".

How to deploy
=============

With docker-compose
-------------------

Execute following commands::

    $ git clone https://github.com/8ayac/buggybase.git
    $ cd buggybase
    $ docker-compose up -d

Go to http://127.0.0.1:5000

With vagrant
-------------------

Execute following commands::

    $ vagrant plugin install vagrant-docker-compose
    $ git clone https://github.com/8ayac/buggybase.git
    $ cd buggybase
    $ vagrant up

Go to http://127.0.0.1:5000