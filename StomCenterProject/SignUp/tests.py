from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Day, User, DoctorDay, Order
from django.contrib.auth.models import Group


class DayTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='maksim', password='123456')
        self.manager = User.objects.create_user(username='manager', password='123456')
        self.group1 = Group.objects.create(name='doctor')
        self.group2 = Group.objects.create(name='manager')
        self.user.groups.add(self.group1)
        self.manager.groups.add(self.group2)
        self.day = Day.objects.create(name='monday')

    def test_get_day(self):
        self.url = reverse('day')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)

    def test_get_day_as_doctor(self):
        self.client.login(username='maksim', password='123456')
        self.url = reverse('day')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)

    def test_post_day_anonymous(self):
        self.url = reverse('day')
        data = {'name': 'tuesday'}
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, 403)

    def test_post_day_doctor(self):
        self.client.login(username='maksim', password='123456')
        self.url = reverse('day')
        data = {'name': 'tuesday'}
        self.response = self.client.post(self.url, data)
        self.assertEqual(self.response.status_code, 201)

    def test_put_day_manager(self):
        self.client.login(username='manager', password='123456')
        self.url = reverse('day_detail', args=(self.day.id,))
        data = {'name': 'moooon'}
        self.response = self.client.put(self.url, data)
        self.assertEqual(self.response.status_code, 202)

    def test_put_day_doctor(self):
        self.client.login(username='maksim', password='123456')
        self.url = reverse('day_detail', args=(self.day.id,))
        data = {'name': 'moooon'}
        self.response = self.client.put(self.url, data)
        self.assertEqual(self.response.status_code, 403)


class OrderTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('order')
        self.own_client = Group.objects.create(name='client')
        self.mng=Group.objects.create(name='manager')
        self.doctor = Group.objects.create(name='doctor')
        self.user1 = User.objects.create_user(username='client', password='123456')
        self.user2 = User.objects.create_user(username='doctor', password='123456')
        self.user3 = User.objects.create_user(username='client1', password='123456')
        self.user4 = User.objects.create_user(username='manager', password='123456')
        self.user1.groups.add(self.own_client)
        self.user2.groups.add(self.doctor)
        self.user3.groups.add(self.own_client)
        self.user4.groups.add(self.mng)
        self.day = Day.objects.create(name='monday')
        self.doctorday = DoctorDay.objects.create(day=self.day, doctor=self.user2)

        self.order1 = Order.objects.create(client=self.user1, day=self.day, doctor=self.user2)
        self.order2 = Order.objects.create(client=self.user1, day=self.day, doctor=self.user2)
        self.order3 = Order.objects.create(client=self.user3, day=self.day, doctor=self.user2)

    def test_order_get_doctor(self):
        self.client.login(username='doctor', password='123456')
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, 200)

    def test_order_get_client1(self):
        self.client.login(username='client', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, "1")

    def test_order_get_client2(self):
        self.client.login(username='client1', password='123456')
        self.response = self.client.get(self.url)
        self.assertContains(self.response, "3")

    def test_post_order(self):
        self.client.login(username='client',password='123456')
        data={
            'day':self.day.id,
            'doctor':self.user2.id
        }
        self.response=self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,201)

    def test_post_order_by_doctor(self):
        self.client.login(username='doctor',password='123456')
        data={
            'day':self.day.id,
            'doctor':self.user2.id
        }
        self.response=self.client.post(self.url,data)
        self.assertEqual(self.response.status_code,403)

    def test_update_order_manager(self):
        self.url=reverse('order_detail',args=(self.order1.id))
        self.client.login(username='manager',password='123456')
        data={
            'day':self.day.id,
            'doctor':self.user2.id
        }
        self.response=self.client.put(self.url,data)
        self.assertEqual(self.response.status_code,202)

    def test_update_order_doctor(self):
        self.url=reverse('order_detail',args=(self.order1.id))
        self.client.login(username='doctor',password='123456')
        data = {
            'day': self.day.id,
            'doctor': self.user2.id
        }
        self.response = self.client.put(self.url, data)
        self.assertEqual(self.response.status_code, 403)