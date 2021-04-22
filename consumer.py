import pika
import sqlite3

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/',
                                                               pika.PlainCredentials("guest", "guest")))
channel = connection.channel()

reverse_number = 0


def recursive_reverse(number):
    global reverse_number
    if number > 0:
        reminder = number % 10
        reverse_number = (reverse_number * 10) + reminder
        recursive_reverse(number // 10)
    return reverse_number


def callback(ch, method, properties, body):
    number = body.decode("utf-8")

    try:
        conn = sqlite3.connect('database.db')

        cur = conn.cursor()
        cur.execute("UPDATE data SET result_2={} WHERE result_1={};".format(recursive_reverse(int(number)), number))
        conn.commit()
    except Exception as e:
        print(e)

    print(body.decode("utf-8"))


channel.basic_consume(queue='test-q', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
