from django.db import models

class persons(models.Model);
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

class messages(models.Model);
    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        #ordering = ["Jeg ved det ikke"]

    message = models.CharField("Message")
    viewed = models.DateTimeField("Viewed", blank=True, None=True)
    

