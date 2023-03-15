from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_email = models.CharField(max_length=30)
    user_pw = models.CharField(max_length=20)

    def __str__(self):
        return self.user_email + " / id : " + str(self.user_id)

class Note(models.Model):
    note_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    user_id = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column="user_id")

    def __str__(self):
        return self.user_name

class PostIt(models.Model):
    post_id = models.AutoField(primary_key=True)

    anonymous = models.BooleanField()
    writer = models.CharField(max_length=20)
    content_text = models.TextField()

    note_id = models.ForeignKey("Note", related_name="note", on_delete=models.CASCADE, db_column="note_id")

    def __str__(self):
        return self.writer