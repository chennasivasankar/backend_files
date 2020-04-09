from django.db import models
from .constants import *
# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    profile_pic=models.URLField()


class Post(models.Model):
    content=models.CharField(max_length=1000)
    posted_at=models.DateTimeField()
    posted_by=models.ForeignKey(User,
            on_delete=models.CASCADE,
            related_name='posts'
        )


class Comment(models.Model):
    content=models.CharField(max_length=1000)
    commented_at=models.DateTimeField()
    commented_by=models.ForeignKey(User,
            on_delete=models.CASCADE
        )
    post=models.ForeignKey(Post,
            on_delete=models.CASCADE,
            related_name='comments'
        )
    parent_comment=models.ForeignKey('self',
        on_delete=models.CASCADE,
        related_name='reply_comments',
        null=True
        )


class Reaction(models.Model):
    post=models.ForeignKey(Post,
            on_delete=models.CASCADE,
            related_name='post_reactions',
            null=True
        )
    comment=models.ForeignKey(Comment,
            on_delete=models.CASCADE,
            related_name='comment_reactions',
            null=True
        )
    reaction_choices=(
        ('WOW','WOW'),
        ('LIT','LIT'),
        ('HAHA','HAHA'),
        ('THUMBS-UP','THUMBS-UP'),
        ('THUMBS-DOWN','THUMBS-DOWN'),
        ('ANGRY','ANGRY'),
        ('SAD','SAD')
        )
    reaction=models.CharField(
            max_length=100,
            choices=ReactionEnum.choices_tuple()
        )
    reacted_at=models.DateTimeField()
    reacted_by=models.ForeignKey(User,
            related_name='replied_to',
            on_delete=models.CASCADE
        )
    

