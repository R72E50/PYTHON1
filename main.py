from application import create_app


app = create_app()


app.run(port=7000, debug=True)