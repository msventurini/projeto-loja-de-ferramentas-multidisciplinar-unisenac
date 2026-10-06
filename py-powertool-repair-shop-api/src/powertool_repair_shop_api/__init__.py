# from .config.connection import get_connection
from .views.app import app

def main() -> None:
    app.run(debug=True)


if __name__ == '__main__':
    main()