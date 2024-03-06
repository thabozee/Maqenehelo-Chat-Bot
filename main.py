from src.view.app import build

if __name__ == "__main__":
    app = build()
    app.run(debug=True, use_reloader=True)
