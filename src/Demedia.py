import json

import requests


class Debmedia:
    def fake_entry(self, consultorio: str, paciente: str, token: str, pantallas: list[int]):
        url = "https://debq2.debmedia.com/api/screen/fakeentry"

        payload = self.__get_payload(pantallas, paciente, consultorio)
        headers = {
            'x-api-key': token,
            'Content-Type': 'application/json'
        }
        return requests.request("POST", url, headers=headers, data=payload).status_code

    def __get_payload(self, screen_ids: list[int], turno: str, puesto: str):
        return json.dumps({
            "screen.ids": screen_ids,
            "column2": puesto,
            "column0": turno
        })
