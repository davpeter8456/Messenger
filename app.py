from src import create_app
import json

HOST = ''
PORT = 0


app = create_app()

if __name__ == "__main__":
    with open("src/data/config.json", encoding="UTF-8") as file_config:
        data_in = json.load(file_config)
        HOST = data_in['HOST']
        PORT = data_in['PORT']
    print(data_in)
    app.run(host=HOST, port=PORT)
