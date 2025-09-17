"""`tdex`, the pokedex for your terminal."""

from cyclopts import App

from tdex.api import sub_app

app = App()


def main() -> None:
    """CLI entrypoint."""
    app.update(sub_app)
    app()


if __name__ == "__main__":
    main()
