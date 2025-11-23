from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Only insert new test data, do not delete anything

        # Create teams
        Team.objects.get_or_create(name='Marvel', defaults={'description': 'Marvel Superheroes'})
        Team.objects.get_or_create(name='DC', defaults={'description': 'DC Superheroes'})

        marvel = Team.objects.filter(name='Marvel').first()
        dc = Team.objects.filter(name='DC').first()

        # Create users using team PKs
        users = [
            User.objects.get_or_create(name='Iron Man', email='ironman@marvel.com', team_id=marvel.pk)[0],
            User.objects.get_or_create(name='Captain America', email='cap@marvel.com', team_id=marvel.pk)[0],
            User.objects.get_or_create(name='Thor', email='thor@marvel.com', team_id=marvel.pk)[0],
            User.objects.get_or_create(name='Superman', email='superman@dc.com', team_id=dc.pk)[0],
            User.objects.get_or_create(name='Batman', email='batman@dc.com', team_id=dc.pk)[0],
            User.objects.get_or_create(name='Wonder Woman', email='wonderwoman@dc.com', team_id=dc.pk)[0],
        ]

        # Create workouts
        workouts = [
            Workout.objects.get_or_create(name='Pushups', description='Upper body', difficulty='Medium')[0],
            Workout.objects.get_or_create(name='Running', description='Cardio', difficulty='Easy')[0],
            Workout.objects.get_or_create(name='Deadlift', description='Strength', difficulty='Hard')[0],
        ]

        # Create activities using user PKs
        Activity.objects.get_or_create(user_id=users[0].pk, type='Running', duration=30)
        Activity.objects.get_or_create(user_id=users[1].pk, type='Pushups', duration=15)
        Activity.objects.get_or_create(user_id=users[3].pk, type='Deadlift', duration=45)

        # Create leaderboard using user PKs
        Leaderboard.objects.get_or_create(user_id=users[0].pk, points=100, rank=1)
        Leaderboard.objects.get_or_create(user_id=users[3].pk, points=90, rank=2)
        Leaderboard.objects.get_or_create(user_id=users[1].pk, points=80, rank=3)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
