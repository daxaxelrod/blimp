from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    balls_shot = models.IntegerField(default=0)


    def __str__(self):
        return "Pk: {}".format(self.pk)


class Game(models.Model):
    good_guy = models.ForeignKey(Player, related_name='good_guy', null=True, blank=True)
    bad_guy = models.ForeignKey(Player, related_name='bad_guy', null=True, blank=True)
    winner = models.ForeignKey(Player, related_name='winner', null=True, blank=True)
    created_at = models.DateField(auto_now_add=True)
    duration = models.DecimalField(max_digits=15, decimal_places=3, default=0)

    #GAME DATA STREAM
    # good guy
    good_guy_position_x = models.FloatField(default=-2.3973)
    good_guy_position_y = models.FloatField(default=2.82932)
    good_guy_position_z = models.FloatField(default=-0.1822)

    good_guy_rotation_x = models.FloatField(default=0)
    good_guy_rotation_y = models.FloatField(default=0)
    good_guy_rotation_z = models.FloatField(default=0)

    good_ship_position_x = models.FloatField(default=-22.09)
    good_ship_position_y = models.FloatField(default=5.33)
    good_ship_position_z = models.FloatField(default=-0.15)

    good_ship_rotation_x = models.FloatField(default=0)
    good_ship_rotation_y = models.FloatField(default=0)
    good_ship_rotation_z = models.FloatField(default=0)


    good_guy_last_key_press = models.CharField(max_length=30, null=True, blank=True)

    # bad guy
    bad_guy_position_x = models.FloatField(default=-2.2453)
    bad_guy_position_y = models.FloatField(default=2.51678)
    bad_guy_position_z = models.FloatField(default=0.7289)

    bad_guy_rotation_x = models.FloatField(default=0)
    bad_guy_rotation_y = models.FloatField(default=0)
    bad_guy_rotation_z = models.FloatField(default=0)

    bad_ship_position_x = models.FloatField(default=40.3)
    bad_ship_position_y = models.FloatField(default=5.9)
    bad_ship_position_z = models.FloatField(default=-2)

    bad_ship_rotation_x = models.FloatField(default=0)
    bad_ship_rotation_y = models.FloatField(default=0)
    bad_ship_rotation_z = models.FloatField(default=0)



    bad_guy_last_key_press = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return 'Good: {0.good_guy}. Bad: {0.bad_guy}. Winner {0.winner}'.format(self)

    class Meta:
        unique_together = ('good_guy', 'bad_guy',)
