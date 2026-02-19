from django.core.management.base import BaseCommand
from api.models import User, Team, Activity, Leaderboard, Workout
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        
        self.stdout.write(self.style.SUCCESS('Existing data deleted'))
        
        # Create Teams
        self.stdout.write('Creating teams...')
        team_marvel = Team.objects.create(
            name='Team Marvel',
            description='Earth\'s Mightiest Heroes fitness team'
        )
        team_dc = Team.objects.create(
            name='Team DC',
            description='Justice League fitness warriors'
        )
        self.stdout.write(self.style.SUCCESS(f'Created teams: {team_marvel.name}, {team_dc.name}'))
        
        # Create Users (Superheroes)
        self.stdout.write('Creating users...')
        marvel_heroes = [
            {'name': 'Iron Man', 'email': 'ironman@marvel.com', 'password': 'stark123'},
            {'name': 'Captain America', 'email': 'cap@marvel.com', 'password': 'shield123'},
            {'name': 'Thor', 'email': 'thor@marvel.com', 'password': 'hammer123'},
            {'name': 'Black Widow', 'email': 'widow@marvel.com', 'password': 'spy123'},
            {'name': 'Spider-Man', 'email': 'spidey@marvel.com', 'password': 'web123'},
            {'name': 'Hulk', 'email': 'hulk@marvel.com', 'password': 'smash123'},
        ]
        
        dc_heroes = [
            {'name': 'Batman', 'email': 'batman@dc.com', 'password': 'bat123'},
            {'name': 'Superman', 'email': 'superman@dc.com', 'password': 'krypton123'},
            {'name': 'Wonder Woman', 'email': 'wonderwoman@dc.com', 'password': 'amazon123'},
            {'name': 'Flash', 'email': 'flash@dc.com', 'password': 'speed123'},
            {'name': 'Aquaman', 'email': 'aquaman@dc.com', 'password': 'atlantis123'},
            {'name': 'Green Lantern', 'email': 'greenlantern@dc.com', 'password': 'will123'},
        ]
        
        marvel_users = []
        for hero in marvel_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password=hero['password'],
                team_id=str(team_marvel.id)
            )
            marvel_users.append(user)
        
        dc_users = []
        for hero in dc_heroes:
            user = User.objects.create(
                name=hero['name'],
                email=hero['email'],
                password=hero['password'],
                team_id=str(team_dc.id)
            )
            dc_users.append(user)
        
        all_users = marvel_users + dc_users
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} superhero users'))
        
        # Create Activities
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Swimming', 'Weightlifting', 'Yoga', 'Boxing']
        
        for user in all_users:
            # Create 5-10 activities per user
            num_activities = random.randint(5, 10)
            for i in range(num_activities):
                activity_type = random.choice(activity_types)
                duration = random.randint(20, 120)  # 20-120 minutes
                distance = round(random.uniform(1, 20), 2) if activity_type in ['Running', 'Cycling', 'Swimming'] else None
                calories = duration * random.randint(5, 15)  # Rough calorie estimation
                days_ago = random.randint(0, 30)
                activity_date = datetime.now() - timedelta(days=days_ago)
                
                Activity.objects.create(
                    user_id=str(user.id),
                    activity_type=activity_type,
                    duration=duration,
                    distance=distance,
                    calories=calories,
                    date=activity_date
                )
        
        total_activities = Activity.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Created {total_activities} activities'))
        
        # Create Leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        for user in all_users:
            user_activities = Activity.objects.filter(user_id=str(user.id))
            total_activities = user_activities.count()
            total_calories = sum(activity.calories for activity in user_activities)
            total_duration = sum(activity.duration for activity in user_activities)
            
            team_name = team_marvel.name if user.team_id == str(team_marvel.id) else team_dc.name
            
            Leaderboard.objects.create(
                user_id=str(user.id),
                user_name=user.name,
                team_id=user.team_id,
                team_name=team_name,
                total_activities=total_activities,
                total_calories=total_calories,
                total_duration=total_duration
            )
        
        # Update ranks based on total calories
        leaderboard_entries = Leaderboard.objects.all().order_by('-total_calories')
        for rank, entry in enumerate(leaderboard_entries, start=1):
            entry.rank = rank
            entry.save()
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(all_users)} leaderboard entries'))
        
        # Create Workouts
        self.stdout.write('Creating workouts...')
        workouts = [
            {
                'name': 'Iron Man Circuit',
                'description': 'High-intensity circuit training inspired by Tony Stark\'s training regime',
                'activity_type': 'Weightlifting',
                'difficulty_level': 'advanced',
                'estimated_duration': 60,
                'estimated_calories': 600
            },
            {
                'name': 'Captain\'s Shield Run',
                'description': 'Endurance running program inspired by Captain America',
                'activity_type': 'Running',
                'difficulty_level': 'intermediate',
                'estimated_duration': 45,
                'estimated_calories': 450
            },
            {
                'name': 'Thor\'s Hammer Strength',
                'description': 'Power lifting workout fit for the God of Thunder',
                'activity_type': 'Weightlifting',
                'difficulty_level': 'advanced',
                'estimated_duration': 90,
                'estimated_calories': 800
            },
            {
                'name': 'Spider-Man Agility',
                'description': 'Agility and flexibility training inspired by Spider-Man',
                'activity_type': 'Yoga',
                'difficulty_level': 'beginner',
                'estimated_duration': 30,
                'estimated_calories': 200
            },
            {
                'name': 'Batman\'s Night Patrol',
                'description': 'Gotham City patrol-inspired cardio workout',
                'activity_type': 'Running',
                'difficulty_level': 'intermediate',
                'estimated_duration': 50,
                'estimated_calories': 500
            },
            {
                'name': 'Superman Flight Training',
                'description': 'High-altitude simulation workout',
                'activity_type': 'Cycling',
                'difficulty_level': 'advanced',
                'estimated_duration': 75,
                'estimated_calories': 700
            },
            {
                'name': 'Wonder Woman Warrior',
                'description': 'Amazon warrior combat training',
                'activity_type': 'Boxing',
                'difficulty_level': 'advanced',
                'estimated_duration': 60,
                'estimated_calories': 650
            },
            {
                'name': 'Flash Speed Sprint',
                'description': 'Speed training inspired by the Fastest Man Alive',
                'activity_type': 'Running',
                'difficulty_level': 'intermediate',
                'estimated_duration': 40,
                'estimated_calories': 400
            },
            {
                'name': 'Aquaman Ocean Swim',
                'description': 'Deep sea swimming endurance training',
                'activity_type': 'Swimming',
                'difficulty_level': 'intermediate',
                'estimated_duration': 55,
                'estimated_calories': 550
            },
            {
                'name': 'Hulk Smash Strength',
                'description': 'Maximum strength training for incredible power',
                'activity_type': 'Weightlifting',
                'difficulty_level': 'advanced',
                'estimated_duration': 70,
                'estimated_calories': 750
            }
        ]
        
        for workout_data in workouts:
            Workout.objects.create(**workout_data)
        
        self.stdout.write(self.style.SUCCESS(f'Created {len(workouts)} workout programs'))
        
        self.stdout.write(self.style.SUCCESS('==================================='))
        self.stdout.write(self.style.SUCCESS('Database population completed!'))
        self.stdout.write(self.style.SUCCESS(f'Teams: {Team.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Users: {User.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Activities: {Activity.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Leaderboard Entries: {Leaderboard.objects.count()}'))
        self.stdout.write(self.style.SUCCESS(f'Workouts: {Workout.objects.count()}'))
        self.stdout.write(self.style.SUCCESS('==================================='))
