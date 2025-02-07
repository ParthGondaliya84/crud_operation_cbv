from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver
from .models import TeamDetail
from django.contrib.auth.models import User


# @receiver(pre_save,sender = TeamDetail)
# def pre_save_signal(sender, instance, *args, **kwargs):
#     print('---------------------------')
#     print('Pre Save')
#     print({'sender':sender})
#     print({'instance':instance})
#     print({'instance':kwargs})
            


@receiver(post_save, sender = TeamDetail)
def post_save_signal(sender, instance, created, **kwargs):
    if created:
        print('new create')
        print({'sender':sender})
        print({'kwargs':kwargs})
        print({'instance':instance})
    else:
        print('update')


# @receiver(post_delete)
# def pre_delete_signal():
#     pass


# @receiver(pre_delete)
# def post_delete_signal():
#     pass