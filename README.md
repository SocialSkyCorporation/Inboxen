back-end
========

The basic idea here is to use [salmon](https://github.com/moggers87/salmon) in two parts:

* recieve email, check this is an alias exists, push message to queue
* watch the queue for new messages, push them into the DB

This will hopefully allow us fine tune the performance of either wwithout worrying about the other

Requires Salmon and Django

Join us in our IRC channel! We're in the #inboxen channel on [MegNet](https://www.megworld.co.uk/irc/)

copyright
=========

This part of Inboxen is licensed under the GPLv3
