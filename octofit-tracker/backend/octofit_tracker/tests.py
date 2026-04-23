from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='Test Team2')
        u = User.objects.create(email='test@example.com', name='Test User', team=t)
        self.assertEqual(str(u), 'test@example.com')
    def test_activity_create(self):
        t = Team.objects.create(name='Test Team3')
        u = User.objects.create(email='test2@example.com', name='Test User2', team=t)
        a = Activity.objects.create(user=u, type='Run', duration=30, date='2026-04-23')
        self.assertEqual(str(a), 'Test User2 - Run (2026-04-23)')
    def test_workout_create(self):
        t = Team.objects.create(name='Test Team4')
        w = Workout.objects.create(name='Test Workout')
        w.suggested_for.set([t])
        self.assertEqual(str(w), 'Test Workout')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test Team5')
        l = Leaderboard.objects.create(team=t, points=42)
        self.assertEqual(str(l), 'Test Team5: 42 pts')
