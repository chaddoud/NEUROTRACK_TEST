import json


class DatabaseDAL:

    @staticmethod
    def load_data(file):
        try:
            with open(f'./data/{file}') as f:
                data = json.load(f)
                return data
        except Exception as e:
            print(str(e))
            return {}
