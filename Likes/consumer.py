import json
import pika
import django
from sys import path
from os import environ

from likes.models import Post


path.append('/home/Projects/Django Projects/RabbitLikeChecker/Likes/Likes/settings.py')
environ.setdefault('DJANGO_SETTINGS_MODULE', 'Likes.settings')
django.setup()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='likes')


def callback(ch, method, properties, body):
    print("Received in likes...")
    print(body)
    data = json.loads(body)
    print(data)

    if properties.content_type == 'post_created':
        post = Post.objects.create(id=data['id'], title=data['title'])
        post.save()
        print("Post created.")
    elif properties.content_type == 'post_updated':
        post = Post.objects.get(id=data['id'])
        post.title = data['title']
        post.save()
        print("Post updated.")
    elif properties.content_type == 'post_deleted':
        post = Post.objects.get(id=data)
        post.delete()
        print("Post deleted.")


channel.basic_consume(queue='likes', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()
