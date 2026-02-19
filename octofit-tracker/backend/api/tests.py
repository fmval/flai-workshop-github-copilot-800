from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from datetime import datetime
from .models import User, Team, Activity, Leaderboard, Workout


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='Test User',
            email='test@example.com',
            password='testpass123'
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertIsNotNone(self.user.created_at)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'Test User')


class TeamModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='Test Team',
            description='A test team'
        )

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertEqual(self.team.description, 'A test team')
        self.assertIsNotNone(self.team.created_at)

    def test_team_str(self):
        self.assertEqual(str(self.team), 'Test Team')


class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='1',
            activity_type='Running',
            duration=30,
            distance=5.0,
            calories=300,
            date=datetime.now()
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'Running')
        self.assertEqual(self.activity.duration, 30)
        self.assertEqual(self.activity.calories, 300)


class UserAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            name='API Test User',
            email='apitest@example.com',
            password='pass123'
        )
        self.list_url = reverse('user-list')

    def test_get_users_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_user(self):
        data = {
            'name': 'New User',
            'email': 'newuser@example.com',
            'password': 'newpass123'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)


class TeamAPITest(APITestCase):
    def setUp(self):
        self.team = Team.objects.create(
            name='API Test Team',
            description='Test team description'
        )
        self.list_url = reverse('team-list')

    def test_get_teams_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_team(self):
        data = {
            'name': 'New Team',
            'description': 'New team description'
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 2)


class ActivityAPITest(APITestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id='1',
            activity_type='Cycling',
            duration=45,
            distance=10.0,
            calories=450,
            date=datetime.now()
        )
        self.list_url = reverse('activity-list')

    def test_get_activities_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_activity(self):
        data = {
            'user_id': '2',
            'activity_type': 'Swimming',
            'duration': 60,
            'distance': 2.0,
            'calories': 600,
            'date': datetime.now().isoformat()
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Activity.objects.count(), 2)


class LeaderboardAPITest(APITestCase):
    def setUp(self):
        self.leaderboard = Leaderboard.objects.create(
            user_id='1',
            user_name='Leader User',
            team_id='1',
            team_name='Leader Team',
            total_activities=10,
            total_calories=5000,
            total_duration=300,
            rank=1
        )
        self.list_url = reverse('leaderboard-list')

    def test_get_leaderboard_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_leaderboard_ordering(self):
        Leaderboard.objects.create(
            user_id='2',
            user_name='Second User',
            team_id='1',
            team_name='Leader Team',
            total_activities=5,
            total_calories=2500,
            total_duration=150,
            rank=2
        )
        response = self.client.get(self.list_url)
        self.assertEqual(response.data[0]['rank'], 1)
        self.assertEqual(response.data[1]['rank'], 2)


class WorkoutAPITest(APITestCase):
    def setUp(self):
        self.workout = Workout.objects.create(
            name='Test Workout',
            description='A test workout',
            activity_type='Running',
            difficulty_level='intermediate',
            estimated_duration=30,
            estimated_calories=300
        )
        self.list_url = reverse('workout-list')

    def test_get_workouts_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_workout(self):
        data = {
            'name': 'New Workout',
            'description': 'New workout description',
            'activity_type': 'Cycling',
            'difficulty_level': 'beginner',
            'estimated_duration': 20,
            'estimated_calories': 200
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Workout.objects.count(), 2)


class APIRootTest(APITestCase):
    def test_api_root(self):
        url = reverse('api-root')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('leaderboard', response.data)
        self.assertIn('workouts', response.data)
