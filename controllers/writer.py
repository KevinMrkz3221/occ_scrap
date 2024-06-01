import json


class VacancyWriter:
    def __init__(self, filew) -> None:
        self.file = filew
        

    def write(self, data):
        with open(self.file, 'r', encoding='utf-8') as f:
            _data = json.load(f)
            f.close()
        _data.append(data)

        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(_data, f, ensure_ascii=False)
        f.close()


        