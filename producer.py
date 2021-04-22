import pika
import sqlite3
from random import randrange

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/',
                                                               pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()


def concat_number(num1, num2):
    digits = len(str(num2))
    num1 = num1 * (10 ** digits)
    num1 += num2
    return num1


number = randrange(1, 10)

new_number = 0
for n in range(1, number+1):
    new_number = concat_number(new_number, n)

try:
    conn = sqlite3.connect('database.db')

    cur = conn.cursor()
    cur.execute("INSERT INTO data(random_number, result_1) VALUES ({}, {});".format(number, new_number))
    conn.commit()
except Exception as e:
    print(e)

channel.basic_publish(exchange='test-e', routing_key='test', body=bytes(str(new_number), 'utf-8'))

connection.close()

