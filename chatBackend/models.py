from django.db import models
import datetime

class persons(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        #ordering = ["Jeg ved det ikke"]

    full_name = models.CharField("Full name", max_length=20)
    email = models.CharField("Email", max_length=100)
    birthdate = models.DateField("Bithdate")
    description = models.CharField("description", max_length=400, blank=True)
    profile_picture = models.ImageField("Profiel Picture", blank=True)
    nickname = models.CharField("Nickname", max_length=20)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
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

    message = models.TextField("Message")
    viewed = models.DateTimeField("Viewed", blank=True, null=True)

    messageFrom = models.ForeignKey("persons", on_delete=models.PROTECT, default=1)
    messageTo = models.ForeignKey("groups", on_delete=models.PROTECT, default=1)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
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

    person = models.ManyToManyField("persons")

    group_name = models.CharField("Name", max_length=20)

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def save(self, *args, **kwargs):
        if not self.id:
            created_at = datetime.datetime.now()

        updated_at = datetime.datetime.now()

        return super(groups, self).save(*args, **kwargs)
