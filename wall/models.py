from django.db import models

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey('login_app.User', related_name="messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self) -> str:
        return f"<Message object: {self.message} {self.user.first_name} ({self.id})>"

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey('login_app.User', related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self) -> str:
        return f"<Comment object: {self.comment} {self.message} {self.user.first_name} ({self.id})>"