from jinja2 import Environment, PackageLoader, select_autoescape
from xhtml2pdf import pisa


def create_template():
    env = Environment(
        loader=PackageLoader(package_name="auto_cv", package_path="templates"),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("template.html")
    rendered_template = template.render()

    with open("index.html", "w") as f:
        f.write(rendered_template)
    with open("output.pdf", "w+b") as pdf_out:
        pisa.CreatePDF(
            src=rendered_template,
            dest=pdf_out,
        )


if __name__ == "__main__":
    print(create_template())
