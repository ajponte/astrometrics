from app import create_app


def main():
    app = create_app()
    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
