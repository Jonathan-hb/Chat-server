from django.db import models
import datetime
import os
import uuid

def get_upload_path(instance, filename):
    return os.path.join(f"profilePics/{instance.id}")


class persons(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        #ordering = ["Jeg ved det ikke"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField("Full name", max_length=20)
    nickname = models.CharField("Nickname", max_length=20)
    email = models.CharField("Email", max_length=100)
    birthdate = models.DateField("Bithdate")
    description = models.CharField("description", max_length=400, blank=True)
    profile_picture = models.ImageField("Profiel Picture", blank=True, upload_to=get_upload_path)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.nickname}"

    def save(self, *args, **kwargs):
        if not self.id:
            created_at = datetime.datetime.now()

        updated_at = datetime.datetime.now()

        return super(persons, self).save(*args, **kwargs)



class messages(models.Model):
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        ordering = ["-created_at"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    message = models.TextField("Message")
    viewed = models.DateTimeField("Viewed", blank=True, null=True)

    messageFrom = models.ForeignKey("persons", on_delete=models.PROTECT, default=1)
    messageTo = models.ForeignKey("groups", on_delete=models.PROTECT, default=1)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.message}"

    def save(self, *args, **kwargs):
        if not self.id:
            created_at = datetime.datetime.now()

        updated_at = datetime.datetime.now()

        return super(messages, self).save(*args, **kwargs)

class groups(models.Model):
    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        ordering = ["-created_at"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    person = models.ManyToManyField("persons")

    group_name = models.CharField("Name", max_length=20)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.group_name}"

    def save(self, *args, **kwargs):
        if not self.id:
            created_at = datetime.datetime.now()

        updated_at = datetime.datetime.now()

        return super(groups, self).save(*args, **kwargs)
