import pika


def publish_messages_to_queue(queue_name, routing_key, messages):
    with pika.BlockingConnection() as connection:
        channel = connection.channel()
        for message in messages:
            channel.basic_publish(queue_name, routing_key, message)
    print "Messages published"
