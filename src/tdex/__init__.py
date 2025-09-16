"""`tdex`, the pokedex for your terminal."""

from cyclopts import App

app = App()


@app.default
def main() -> None:
    """CLI entrypoint."""
    print("Hello from tdex!")


if __name__ == "__main__":
    app()
