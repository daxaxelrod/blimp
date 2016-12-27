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
    good_guy_position_x = models.FloatField(default=-26.82)
    good_guy_position_y = models.FloatField(default=10.49)
    good_guy_position_z = models.FloatField(default=-0.52)

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
    bad_guy_position_x = models.FloatField(default=35.87)
    bad_guy_position_y = models.FloatField(default=10.49)
    bad_guy_position_z = models.FloatField(default=-.52)

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

class Projectile(models.Model):
    start_location_x = models.FloatField()
    start_location_y = models.FloatField()
    start_location_z = models.FloatField()

    firing_force_x = models.FloatField()
    firing_force_y = models.FloatField()
    firing_force_z = models.FloatField()

    shot_by = models.ForeignKey(Player, related_name="projectiles_shot")
    rendered_in_enemy_client = models.BooleanField(default=False)

    game = models.ForeignKey(Game, related_name="projectiles", null=True, blank=True)
