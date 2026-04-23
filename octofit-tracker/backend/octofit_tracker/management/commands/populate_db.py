from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear all data
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Create users (superheroes)
        users = [
            User.objects.create(email='tony@stark.com', name='Tony Stark', team=marvel, is_superhero=True),
            User.objects.create(email='steve@rogers.com', name='Steve Rogers', team=marvel, is_superhero=True),
            User.objects.create(email='bruce@wayne.com', name='Bruce Wayne', team=dc, is_superhero=True),
            User.objects.create(email='clark@kent.com', name='Clark Kent', team=dc, is_superhero=True),
        ]

        # Create activities
        Activity.objects.create(user=users[0], type='Ironman Suit Training', duration=60, date='2026-04-01')
        Activity.objects.create(user=users[1], type='Shield Throwing', duration=45, date='2026-04-02')
        Activity.objects.create(user=users[2], type='Detective Work', duration=90, date='2026-04-03')
        Activity.objects.create(user=users[3], type='Flight', duration=120, date='2026-04-04')

        # Create workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for superheroes')
        w2 = Workout.objects.create(name='Agility Drills', description='Agility and reflex training')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([marvel, dc])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=200)


        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
