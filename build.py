"""Genera la versión estática del portafolio en _site/ para GitHub Pages.

Uso: python build.py
"""
import shutil
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, select_autoescape

from main import CONTEXT

ROOT = Path(__file__).parent
OUT = ROOT / "_site"


def static_url(name: str, path: str) -> str:
    """Sustituye al url_for de Starlette con rutas relativas,
    así la página funciona en cualquier subruta (p. ej. /portafolio/)."""
    if name != "static":
        raise ValueError(f"url_for('{name}') no está soportado en el build estático")
    return "static/" + path.lstrip("/")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT / "static")

    env = Environment(
        loader=FileSystemLoader(ROOT / "templates"),
        autoescape=select_autoescape(["html"]),
    )
    env.globals["url_for"] = static_url

    html = env.get_template("index.html").render(**CONTEXT)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    (OUT / ".nojekyll").touch()
    print(f"Sitio generado en {OUT}")


if __name__ == "__main__":
    main()
