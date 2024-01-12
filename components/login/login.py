from typing import Dict

from kivy.uix.screenmanager import Screen
from requests import post, get
from kivy.logger import Logger
from http import HTTPStatus
from config.constants import API_HOST, LOCAL_DATA


class Login(Screen):

    def login(self):
        print(self.ids.username.text)
        print(self.ids.password.text)
        response = post(url=f'{API_HOST}/auth/login', json={
            "mobile": self.ids.username.text,
            "password": self.ids.password.text
        })
        Logger.info(f'Login API Status: {response.status_code}')
        if response.status_code == HTTPStatus.OK:
            response = response.json()
            token: dict[str, str] = {"Authorization": f"{response.get('token_type')} {response.get('access_token')}"}
            LOCAL_DATA.put('token', **token)
            response = get(url=f'{API_HOST}/auth/getUser', headers=LOCAL_DATA.get('token'))
            Logger.info(f'User Info API Status: {response.status_code}')
            if response.status_code == HTTPStatus.OK:
                LOCAL_DATA.put('user', **response.json())
                self.manager.current = 'home'
            else:
                pass
        else:
            pass
