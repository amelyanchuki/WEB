from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
from user.models import User


def sharp_valid(value):
    if not value.startswitch('#'):
        raise ValidationError(
            f"Invalid value. Maybe '#{value}'?",
            )

class Tag(models.Model):
    name = models.CharField(
        max_length=20,
        validators=[sharp_valid],
        verbose_name="Tag name",
    )
    descript = models.TextField(
        verbose_name="Despirations of tag name.",
    )

    class Meta:
        db_table = "tags"
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name="Title",
    )
    text = models.TextField(
        verbose_name="Text of post.",
    )
    author = models.ForeignKey(
        User, related_name="posts",
        on_delete=models.CASCADE,
    )
    tags = models.ManyToManyField(
        Tag,
        related_name="posts",
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data of create post."
    )
    edited = models.DateTimeField(
        auto_now=True,
        verbose_name= "Date of edit post",
    )
    views = models.BigIntegerField(
        default=0,
        verbose_name="Count of view.",
    )
    is_moderated = models.BooleanField(
        default=False,
        verbose_name="If moderated.",
    )
    class Meta:
        db_table = "post"
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"Post of {self.author}"




class Comment(models.Model):
    author =models.ForeignKey(
        User,
        related_name="comments",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE
    )
    text = models.TextField(
        verbose_name="Text of comment"
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data of create post."
    )
    edited = models.DateTimeField(
        auto_now=True,
        verbose_name= "Date of edit post",
    )
    is_moderated = models.BooleanField(
        default=False,
        verbose_name="If moderated.",
    )
    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self) -> str:
        return f"Comment of {self.post}"
    
