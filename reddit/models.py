from django.db import models
import uuid

class BaseModel(models.Model):
    eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    class Meta: abstract = True

    def get_or_none(cls, **kwargs):
        try:
            return cls.objects.get(**kwargs)
        except cls.DoesNotExist:
            return None

class Votable(BaseModel):
    upvote_count = models.PositiveBigIntegerField(default=0)
    downvote_count = models.PositiveBigIntegerField(default=0)
    class Meta: abstract = True

    def get_score(self):
        return self.upvote_count - self.downvote_count