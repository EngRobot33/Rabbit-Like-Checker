import json
import pika
import django
from sys import path
from os import environ

from posts.models import Post


path.append('/home/Projects/Django Projects/RabbitLikeChecker/Posts/Posts/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'Posts.settings')
django.setup()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='posts', durable=True)


def callback(ch, method, properties, body):
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'post_liked':
        post = Post.objects.get(id=data)
        post.likes += 1
        post.save()
        print("Post likes increased.")


channel.basic_consume(queue='posts', on_message_callback=callback)
print("Started Consuming...")
channel.start_consuming()
channel.close()
