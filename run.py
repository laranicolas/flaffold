from api import app


if __name__ == '__main__':
    app.run(
        host = app.config['GENERAL']['host'],
        port = app.config['GENERAL']['port']
    )