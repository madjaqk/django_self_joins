from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def create_new_user(self, name):
		self.create(name=name)

	def add_friend(self, user_id, friend_id):
		guy = self.get(id=user_id)
		friend = self.get(id=friend_id)
		guy.friends.add(friend)
		# Because this is many-to-many, it's symmetrical by default.  No need to update the friend.

class User(models.Model):
	name = models.CharField(max_length=255)
	friends = models.ManyToManyField('self')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	manager = UserManager()

