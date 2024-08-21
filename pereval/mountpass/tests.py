import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import *
from .serializers import *

'''python manage.py test . - Запускает все тесты
 python manage.py test passapp.tests.PerevalApiTestCase.test_get_list - для запуска одного конкретного теста
 coverage run --source='.' manage.py test . - создает слепок .coverage, при изменении теста команду повторить
 coverage report - по слепку создает отчет в консоли
coverage html - создает папку htmlcov\index.html и в ней отчет
 '''


class PerevalApiTestCase(APITestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='Вершина',
            title='Купол трёх озер',
            other_titles='Купол Актру',
            connect='',
            user=HikeUser.objects.create(
                email='perg@example.com',
                fam='Пергаев',
                name='Владимиир',
                otc='Петрович',
                phone='+13337772548'
            ),
            coords=Coords.objects.create(
                latitude=50.0484,
                longitude=87.79659,
                height=3556
            ),
            level=Level.objects.create(
                winter='1Б',
                spring='1Б',
                summer='1Б',
                autumn='1Б'
            ),
        )
        Image.objects.create(
            pereval=self.pereval_1,
            title='Купол',
            image='https://www.altai-poxod.ru/sites/default/files/styles/flexslider_full/public/programma-day-foto/file/ajax/field_tour_slides/und/form-DGHr3izfiRMbXr_cb9Ew2l5sJMqAH7xgHifg0tYxXlk/kupol002.jpg?itok=muA-WdV1'
        )

        self.pereval_2 = Pereval.objects.create(
            beauty_title='Перевал',
            title='Учитель',
            other_titles='',
            connect='Северо-Чуйский хребет',
            user=HikeUser.objects.create(
                email='param@example.com',
                fam='Парамонов',
                name='Антон',
                otc='Арнольдович',
                phone='+341113332800'
            ),
            coords=Coords.objects.create(
                latitude=50.0834,
                longitude=87.77923,
                height=3000
            ),
            level=Level.objects.create(
                winter='1А',
                spring='1А',
                summer='1А',
                autumn='1А'
            ),
        )
        Image.objects.create(
            pereval=self.pereval_2,
            title='Перевал Учитель',
            image='https://i.ytimg.com/vi/Pxg2nCNPOvM/maxresdefault.jpg'
        )

        self.pereval_3 = Pereval.objects.create(
            beauty_title='Перевал',
            title='Кату-Ярык',
            other_titles='',
            connect='Долина Чулышмана',
            user=HikeUser.objects.create(
                email='perg@example.com',
                fam='Пергаев',
                name='Владимиир',
                otc='Петрович',
                phone='+13337772548'
            ),
            coords=Coords.objects.create(
                latitude=50.0484,
                longitude=87.79659,
                height=3556
            ),
            level=Level.objects.create(
                winter='1Б',
                spring='1Б',
                summer='1Б',
                autumn='1Б'
            ),
        )
        Image.objects.create(
            pereval=self.pereval_3,
            title='Кату-Ярык',
            image='https://avatars.dzeninfra.ru/get-zen_doc/271828/pub_653691a0ec70fb565bf1fafc_653692f1d11ae01d2a6d8674/scale_1200'
        )
    def test_get_list(self):
        url = reverse('pereval-list')
        response = self.client.get(url)
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_2, self.pereval_3], many=True).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(len(response.data), 3)
    def test_get_detail(self):
        url = reverse('pereval-detail', args=(self.pereval_1.id,))
        response = self.client.get(url)
        serializer_data = PerevalSerializer(self.pereval_1).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_list_email(self):
        url = reverse('pereval-list')
        response = self.client.get(f'{url}?user__email=perg@example.com')
        serializer_data = PerevalSerializer([self.pereval_1, self.pereval_3], many=True).data
        self.assertEquals(response.data, serializer_data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(len(response.data), 2)

    def test_create_pereval(self):
        url = reverse('pereval-list')
        data = {
            'beauty_title': 'dfgh',
            'title': 'fghm',
            'other_titles': 'ghjи',
            'connect': 'cvbn',
            'add_time': '',
            'user': {
                'fam': 'hhhh',
                'name': 'hhhh',
                'otc': 'sdfgh',
                'email': 'tqw@example.com',
                'phone': '88888888888'
            },
            "coords": {
                'latitude': 77,
                'longitude': 567,
                'height': 5879
            },
            "level": {
                "winter": "1A",
                "spring": "1A",
                "summer": "1A",
                "autumn": "1A"
            },
            "images": [
                {
                    "image": 'http://lagonaki-otdyh.ru/azishkij-pereval-03.jpg',
                    "title": "dfgh"
                }
            ],
        }
        json_data = json.dumps(data)
        response = self.client.post(path=url, content_type='application/json', data=json_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class PerevalSerializerTestCase(TestCase):
    def setUp(self):
        self.pereval_1 = Pereval.objects.create(
            beauty_title='Вершина',
            title='Купол трёх озер',
            other_titles='Купол Актру',
            connect='хребет',
            add_time='21-08-2024 04:05:02',
            user=HikeUser.objects.create(
                email='perg@example.com',
                fam='Перов',
                name='Владимир',
                otc='Петрович',
                phone='+13337772548'
            ),
            coords=Coords.objects.create(
                latitude=50.0484,
                longitude=87.79659,
                height=3556
            ),
            level=Level.objects.create(
                winter='1Б',
                spring='1Б',
                summer='1Б',
                autumn='1Б'
            ),
        )
        Image.objects.create(
            pereval=self.pereval_1,
            title='Купол',
            image='https://www.altai-poxod.ru/sites/default/files/styles/flexslider_full/public/programma-day-foto/file/ajax/field_tour_slides/und/form-DGHr3izfiRMbXr_cb9Ew2l5sJMqAH7xgHifg0tYxXlk/kupol002.jpg?itok=muA-WdV1'
        )


    def test_check(self):
        serializer_data = PerevalSerializer(self.pereval_1).data
        time = self.pereval_1.add_time.strftime('%d-%m-%Y %H:%M:%S')
        expected_data = {
                'id': 1,
                'beauty_title': 'Вершина',
                'title': 'Купол трёх озер',
                'other_titles': 'Купол Актру',
                'connect': 'хребет',
                'add_time': f'{time}',
                'user': {
                    'email': 'perg@example.com',
                    'phone': '+13337772548',
                    'fam': 'Перов',
                    'name': 'Владимир',
                    'otc': 'Петрович',
                },
                'coords': {
                    'latitude': '50.048400',
                    'longitude': '87.796590',
                    'height': 3556
                },
                'status': 'new',
                'level': {
                    'winter': '1Б',
                    'summer': '1Б',
                    "autumn": '1Б',
                    'spring': '1Б',
                },
                'images': [
                    {
                        'image': 'https://www.altai-poxod.ru/sites/default/files/styles/flexslider_full/public/programma-day-foto/file/ajax/field_tour_slides/und/form-DGHr3izfiRMbXr_cb9Ew2l5sJMqAH7xgHifg0tYxXlk/kupol002.jpg?itok=muA-WdV1',
                        'title': 'Купол'
                    }
                ],
            }

        self.assertEquals(serializer_data, expected_data)